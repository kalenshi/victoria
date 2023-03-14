import os
import secrets

from flask import current_app
from PIL import Image


def save_picture(form_picture):
    """
    Saves the picture provided as th current users_bp profile picture

    Args:
        form_picture (str): the location on the user's machine to the picture

    Return:
        file_name (str) : The name of the new profile picture
    """
    random_hex = secrets.token_hex(16)
    _, file_ext = os.path.splitext(form_picture.filename)
    file_name = f"{random_hex}{file_ext.lower()}"
    picture_path = os.path.join(current_app.root_path, "static", "media", "profile_pics", file_name)
    # Resize the image before saving it
    output_size = (125, 125)  # The dimensions of the photo we want
    try:
        image = Image.open(form_picture)
        image.thumbnail(output_size)
        image.save(picture_path)
    except FileNotFoundError:
        file_name = "default.png"

    return file_name
