WEB_MPD_URL = "http://music.lan"
DEBUG = False

try:
    from local_config import *
except ImportError:
    pass
