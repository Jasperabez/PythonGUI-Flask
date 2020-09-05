from flask import Flask
from flaskwebgui import FlaskUI
import sys, os

if getattr(sys, 'frozen', False):
    base_dir = os.path.join(sys._MEIPASS)
    app = Flask(__name__,
        static_folder=os.path.join(base_dir, 'static'),
        template_folder=os.path.join(base_dir, 'templates'))
else:
    app = Flask(__name__)

ui = FlaskUI(app)
app.config.from_object('config')

from . import views