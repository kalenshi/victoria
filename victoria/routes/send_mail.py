

from flask import url_for
from flask_mail import Message

from victoria import mail, app


def send_reset_email(user):
    """
    Sends an email to the email of user

    Args:
        user (User) : The user model with it's attributes

    Returns:
        bol : returns True
    """
    token = user.get_reset_token()

    body = f"""
           To reset your password, visit the following link:
           <a href='{url_for(f"reset_password", token=token, _external=True)}'>Reset</a>
           <p>If you did not make this request, then simply ignore this email and no 
           changes will be made</p>
    """
    message = Message(
        subject="Reset password",
        recipients=[user.email],
        sender=app.config.get("MAIL_USERNAME"),
        html=f"<div class='container'><h2>Please just follow the link</h2><p>{body}</p></div>",
    )

    mail.send(message=message)

    return True
