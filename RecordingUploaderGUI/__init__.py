from flask import Flask
from webui import WebUI
import PySide2.QtGui as gui
import sys, os

import config

icon_path = os.path.join(os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__)), config.ICON_RELATIVE_PATH)

if getattr(sys, 'frozen', False):
    base_dir = os.path.join(sys._MEIPASS)
    app = Flask(__name__,
        static_folder=os.path.join(base_dir, 'static'),
        template_folder=os.path.join(base_dir, 'templates'))
else:
    app = Flask(__name__)

ui = WebUI(app, icon_path=icon_path, app_name=config.WINDOW_TITLE)
app.config.from_object('config')

from . import views