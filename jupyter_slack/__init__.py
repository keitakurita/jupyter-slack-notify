from .jupyter_slack import notify_self, MessengerMagics

try:
    ip = get_ipython()
    ip.register_magics(MessengerMagics)
except:
    pass
