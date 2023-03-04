"""
This module will contain all the configuration for our site
"""
import os


class Config:
    """
    Config  base class
    """
    SECRET_KEY = os.environ.get("SECRET_KEY", "ddbbb12fff42fa84db757a1bf1027f63")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "server170.web-hosting.com",
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USE_TLS = False,
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
