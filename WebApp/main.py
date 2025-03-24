"""start the API and UI threads"""

from app.api import start_api_thread
from app.ui import run_ui

if __name__ == "__main__":
    start_api_thread()
    run_ui()
