import socket

#My laptop is name 'Guinsly-thinkpad-lenovo'
if 'MRT' in socket.gethostname():
    from .development import *
    print('--dev--settings--')
else:
    from .production import *
    #print('prod--settings')
