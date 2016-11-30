import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, render_template
from flask.ext.script import Manager, Server
from flask_init import app
from flask_script import Manager


manager = Manager(app)

if __name__ == '__main__':
    app.debug = False
    app.run(host="0.0.0.0", port=5000)
