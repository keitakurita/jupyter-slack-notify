import os
import requests


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


if __name__ == '__main__':
    notify_self("hello world")
