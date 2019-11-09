import pytest
import jupyter_slack

def test_notify():
    jupyter_slack.notify_self("hello world")
