from slackclient import SlackClient
import os


def notify_self(message):
    slack_token = os.environ["SLACK_TOKEN"]
    slack_id = os.environ["SLACK_ID"]
    sc = SlackClient(slack_token)
    return sc.api_call("chat.postMessage", channel="@" + slack_id, text=message)


if __name__ == '__main__':
    notify_self("hello world")
