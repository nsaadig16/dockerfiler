import os
from dotenv import load_dotenv

load_dotenv()

TEMPLATES_PATH = os.getenv("TEMPLATES_PATH", "templates")
OUTPUT_PATH = os.getenv("OUTPUT_PATH", "Dockerfile")
