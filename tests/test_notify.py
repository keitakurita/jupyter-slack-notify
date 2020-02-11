import pytest
import jupyter_slack

def test_notify():
    jupyter_slack.notify_self("hello world")

def test_context_manager_no_exception():
    with jupyter_slack.Monitor("test no exception", time=False):
        pass

def test_context_manager_no_exception_time():
    with jupyter_slack.Monitor("test no exception timed", time=True):
        pass

def test_context_manager_exception():
    with pytest.raises(ValueError, match="AAAAA"):
        with jupyter_slack.Monitor("test exception", time=False):
            raise ValueError("AAAAA")

def test_context_manager_exception_tb():
    def external_fn():
        raise ValueError("AAAAA")
    def error_fn():
        def inner_error_fn():
            external_fn()
        inner_error_fn()
    with pytest.raises(ValueError):
        with jupyter_slack.Monitor("test exception", time=False, send_full_traceback=True):
            error_fn()

def test_decorater_exception_tb():
    def external_fn():
        raise ValueError("AAAAA")
    @jupyter_slack.Monitor("test decorator exception", send_full_traceback=True)
    def error_fn():
        def inner_error_fn():
            external_fn()
        inner_error_fn()

    with pytest.raises(ValueError):
        error_fn()

def test_silent():
    with jupyter_slack.Monitor("silent! this should not be sent", silent=True):
        pass
