import os
from flask import Blueprint

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATES_FOLDER = os.path.join(BASE_DIR, "templates")

main_bp = Blueprint("main_bp", __name__, template_folder=TEMPLATES_FOLDER)
