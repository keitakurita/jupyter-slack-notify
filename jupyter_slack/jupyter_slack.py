import os
import requests
from IPython.core import magic_arguments
from IPython.core.magics import ExecutionMagics
from IPython.core.magic import cell_magic, magics_class


def notify_self(message):
    slack_token = os.environ["SLACK_TOKEN"]
    slack_id = os.environ["SLACK_ID"]
    parameters = {
        "token": slack_token,
        "channel": "@" + slack_id,
        "text": message
    }
    r = requests.post("https://slack.com/api/chat.postMessage", params=parameters)
    return r.text


@magics_class
class MessengerMagics(ExecutionMagics):

    def __init__(self, shell):
        super().__init__(shell)

    @cell_magic
    @magic_arguments.magic_arguments()
    @magic_arguments.argument("message", type=str)
    def notify(self, line="", cell=None):
        args = magic_arguments.parse_argstring(self.notify, line)
        mess = args.message.replace("\"", "")
        try:
            self.shell.ex(cell)
            notify_self("Finished {}".format(mess))
        except BaseException as e:
            notify_self("Error while {}: {}".format(mess, e.__repr__()))
            raise e
