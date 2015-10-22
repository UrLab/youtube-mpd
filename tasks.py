from subprocess import check_output
from flask.ext.rq import job
import config
import os
import tempfile
import shutil


@job
def convert_and_add(url, options):
    name_tpl = "%(title)s.%(ext)s"
    output_dir = tempfile.mkdtemp()
    output_path = os.path.join(output_dir, name_tpl)

    check_output(["youtube-dl", "-x", url, "--audio-format", "mp3", "--restrict-filenames", "-o", output_path])

    filename = os.listdir(output_dir)[0]

    file_path = os.path.join(output_dir, filename)
    file_destination = os.path.join(config.DESTINATION, filename)

    shutil.copy(file_path, file_destination)
    os.unlink(file_destination)
    os.unlink(output_dir)

    assert config.DESTINATION.startswith(config.MPD_MUSIC_DIR)

    relative_path = file_destination.lstrip(config.MPD_MUSIC_DIR)
    check_output(["mpc", "update", "--wait", relative_path])

    command = "add" if options['add'] else "insert"
    check_output(["mpc", command, relative_path])
