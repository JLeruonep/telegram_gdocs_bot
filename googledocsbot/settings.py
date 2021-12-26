import os
from dotenv import load_dotenv


load_dotenv()

CREDENTIALS = {
    "type": "service_account",
    "project_id": "lustrous-vertex-335306",
    "private_key_id": os.getenv("PRIVATE_KEY_ID", ""),
    "private_key": os.getenv("PRIVATE_KEY", "").replace('\\n', '\n'),
    "client_email": "google-sheets-api@lustrous-vertex-335306.iam.gserviceaccount.com",
    "client_id": os.getenv("CLIENT_ID", ""),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/google-sheets-api%40lustrous-vertex-"
                            "335306.iam.gserviceaccount.com"
}

TG_TOKEN = os.getenv('TG_TOKEN', '')
SHEET_ID = '1PqmtvnZebPpw1xt4Dk0IbT-etpfzzMb5cHoNjsJGeeI'
SHEET_URL= 'https://docs.google.com/spreadsheets/d/1PqmtvnZebPpw1xt4Dk0IbT-etpfzzMb5cHoNjsJGeeI/edit#gid=0'

USER_ID = '344604964'