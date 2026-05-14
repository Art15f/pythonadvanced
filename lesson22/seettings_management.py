from pydantic import BaseSettings

class Settings(BaseSettings):
    app_email: str
    admin_email: str
    item_per_user: int = 50

settings = Settings()