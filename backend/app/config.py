import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "spaceapi.db"),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-jwt-secret")

    NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
    NASA_BASE_URL = os.getenv("NASA_BASE_URL", "https://api.nasa.gov")
    EPIC_BASE_URL = os.getenv("EPIC_BASE_URL", "https://api.nasa.gov/EPIC")
