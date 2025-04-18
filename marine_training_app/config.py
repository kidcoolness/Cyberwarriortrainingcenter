import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")  # Set a secure key
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///instance/app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Toggle Online/Offline Mode
    IS_ONLINE = os.getenv("IS_ONLINE", "true").lower() == "true"
