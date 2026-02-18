import os
from dotenv import load_dotenv

# loading API key and secret
load_dotenv()


class Settings:
    TM_API_KEY: str = os.getenv("TM_CONSUMER_KEY")
    DB_URL: str = os.getenv("DATABASE_URL", "sqlite:///./ticket_tracker.db")


settings = Settings()
