"""
Configuration module for Quotex API client.
Contains essential settings and credentials for API authentication.
"""

import sys
from pathlib import Path
import os
import json
import sys
# Browser user agent for API requests
USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"

# Base directory setup
base_dir = Path(__file__).parent.parent

# Authentication credentials
email = 'govindkhapare2001@gmail.com'
password = 'Akshay@2001'

# Validate credentials
if not email or not password:
    print("Email and password cannot be left blank...")
    sys.exit()

# Browser instance directory
user_data_dir = "browser/instance/quotex.default"


def load_session(user_agent):
    output_file = Path(
        resource_path(
            "session.json"
        )
    )
    if os.path.isfile(output_file):
        with open(output_file) as file:
            session_data = json.loads(
                file.read()
            )
    else:
        output_file.parent.mkdir(
            exist_ok=True,
            parents=True
        )
        session_dict = {
            "cookies": None,
            "token": None,
            "user_agent": user_agent
        }
        session_result = json.dumps(session_dict, indent=4)
        output_file.write_text(
            session_result
        )
        session_data = json.loads(
            session_result
        )
    return session_data


def update_session(session_data):
    output_file = Path(
        resource_path(
            "session.json"
        )
    )
    session_result = json.dumps(session_data, indent=4)
    output_file.write_text(
        session_result
    )
    session_data = json.loads(
        session_result
    )
    return session_data



def resource_path(relative_path: str | Path) -> Path:
    global base_dir
    """Get absolute path to resource, works for dev and for PyInstaller"""
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        base_dir = Path(sys._MEIPASS)
    return base_dir / relative_path
