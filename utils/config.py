import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL: str = os.getenv("BASE_URL", "https://www.saucedemo.com")
    STANDARD_USER: str = os.getenv("STANDARD_USER", "standard_user")
    LOCKED_USER: str = os.getenv("LOCKED_USER", "locked_out_user")
    PROBLEM_USER: str = os.getenv("PROBLEM_USER", "problem_user")
    PASSWORD: str = os.getenv("PASSWORD", "secret_sauce")
    HEADLESS: bool = os.getenv("HEADLESS", "true").lower() == "true"
    BROWSER: str = os.getenv("BROWSER", "chromium")
