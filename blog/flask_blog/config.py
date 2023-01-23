import os


class Config:
    
    SECRET_KEY = os.environ.get("91a6dd8b9b66a75b14a544c2c1bf0767")
    SQLALCHEMY_DATABASE_URI = os.environ.get("sqlite:///site.db")
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")