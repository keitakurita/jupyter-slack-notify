from .jupyter_slack import notify_self, Monitor, MessengerMagics

try:
    ip = get_ipython()
    ip.register_magics(MessengerMagics)
except:
    pass
