WEB_MPD_URL = "http://music.lan"
DESTINATION = "/var/lib/mpd/music/azog/imported/"
MPD_MUSIC_DIR = "/var/lib/mpd/music/"
TIMEOUT = 10 * 60

ROOT_URL = "/"

DEBUG = False

try:
    from local_config import *
except ImportError:
    pass
