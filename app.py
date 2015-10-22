from flask import Flask, render_template, request, redirect
from subprocess import check_output
from flask.ext.rq import RQ
import tasks
import re
import config

app = Flask(__name__)
RQ(app)


@app.route("/")
def home():
    return render_template('skel.html', root=config.ROOT_URL)


@app.route("/add", methods=['POST'])
def submit_url():
    url = request.form['url']
    add = request.form['command'] == "add"

    is_soundcloud = re.match(r'^https?://(www\.)?soundcloud.com/', url) is not None

    if is_soundcloud:
        check_output(["mpc", "load", "soundcould://url/" + url])
    else:
        tasks.convert_and_add.delay(url, {'add': add})

    return redirect(config.WEB_MPD_URL)


if __name__ == "__main__":
    app.run(debug=config.DEBUG)
