import os
import time
import warnings
import requests
from IPython.core import magic_arguments
from IPython.core.magics import ExecutionMagics
from IPython.core.magic import cell_magic, magics_class


def notify_self(message):
    slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if slack_webhook_url is not None:
        r = requests.post(slack_webhook_url, json={"text": message})
        return r.text, message
    else:
        slack_token = os.getenv("SLACK_TOKEN")
        slack_id = os.getenv("SLACK_ID")
        if slack_token is not None and slack_id is not None:
            warnings.warn("Slack tokens are a legacy feature and may be deprecated at any time: "
                          "Consider moving to webhooks (see https://api.slack.com/messaging/webhooks) "
                          "for more details")
            parameters = {
                "token": slack_token,
                "channel": "@" + slack_id,
                "text": message
            }
            r = requests.post("https://slack.com/api/chat.postMessage", params=parameters)
            return r.text, message
        else:
            raise ValueError("Either $SLACK_WEBHOOK_URL must be set "
                             "(see https://api.slack.com/messaging/webhooks) "
                             "or both $SLACK_TOKEN and $SLACK_ID must be set "
                             "(see https://api.slack.com/custom-integrations/legacy-tokens)")

class Monitor:
    def __init__(self, msg, time=False):
        self.msg = msg
        self.time = time

    @staticmethod
    def construct_time_mess(elapsed):
        day = elapsed // (24 * 3600)
        elapsed = elapsed % (24 * 3600)
        hour = elapsed // 3600
        elapsed %= 3600
        minutes = elapsed // 60
        elapsed %= 60
        seconds = round(elapsed, 1)
        time_mess = ""
        if day > 0:
            time_mess += " {} days".format(day)
        if hour > 0:
            time_mess += " {} hours ".format(hour)
        if minutes > 0:
            time_mess += " {} minutes".format(minutes)
        if seconds > 0:
            time_mess += " {} seconds".format(seconds)
        return time_mess

    def __enter__(self):
        self._start = time.time()
        return self

    def __exit__(self, exeception_type, exception_value, traceback):
        if exception_value is None:
            if self.time:
                elapsed = time.time() - self._start
                msg = "Finished {} in {}".format(self.msg, self.construct_time_mess(elapsed))
            else: msg = "Finished {}".format(self.msg)
            notify_self(msg)
        else:
            msg = "Error while {}'\n```\n{!r}\n```".format(self.msg, exception_value)
            notify_self(msg)
            raise exception_value.with_traceback(traceback)

@magics_class
class MessengerMagics(ExecutionMagics):

    def __init__(self, shell):
        super().__init__(shell)

    @cell_magic
    @magic_arguments.magic_arguments()
    @magic_arguments.argument("message", type=str)
    @magic_arguments.argument("--time", "-t", action="store_true")
    def notify(self, line="", cell=None):
        args = magic_arguments.parse_argstring(self.notify, line)
        mess = args.message.replace("\"", "")
        with Monitor(mess, time=args.time):
            self.shell.ex(cell)
