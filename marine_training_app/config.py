import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")  # Set a secure key
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "postgresql://cyberwarriortrainingcenter_user:Hlkpt8eFc9qovjNPB6A42MEmovJeNyc0@dpg-d00pcaidbo4c73digq20-a/cyberwarriortrainingcenter")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Toggle Online/Offline Mode
    IS_ONLINE = os.getenv("IS_ONLINE", "true").lower() == "true"

#postgresql://cyberwarriortrainingcenter_user:Hlkpt8eFc9qovjNPB6A42MEmovJeNyc0@dpg-d00pcaidbo4c73digq20-a/cyberwarriortrainingcenter