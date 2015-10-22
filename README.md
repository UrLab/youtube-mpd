# A web UI to add youtube videos and soundcloud tubes to mpd

This is _python3_ software (future is now)


## How to

Dependencies:

 * `ffmpeg` or `avconv`
 * `redis-server`


Installation :

    pyvenv-3.4 ve
    source ve/bin/activate
    pip install -r requirements.txt

Run :

    python app.py & rqworker

Configuration (put your values in `local_config.py`):

 * `WEB_MPD_URL`: url to be redirected to on successull import
 * `DEBUG`: speaks for itself
 * `DESTINATION`: final destination for converted videos (must be contained within `MPD_MUSIC_DIR` and be writable)
 * `MPD_MUSIC_DIR`: root directory for mpd music files
 * `ROOT_URL`: defaults to `/`. Ca be used to host youtube-mpd in a sub-url (like: `http://music.lan/youtube/`). Must begin and end with a slash
 * `TIMEOUT`: time (in seconds) before a worker (converting viedos to mp3) timeouts (defaults to 10m) (_NOT USED FOR NOW_)

# Authors

 * @etnarek
 * @C4ptainCrunch
