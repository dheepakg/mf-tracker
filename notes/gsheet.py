# Refer - https://towardsdatascience.com/turn-google-sheets-into-your-own-database-with-python-4aa0b4360ce7

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os

# Connect to Google Sheets
scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("./notes/mf-tracker-gs-creds.json", scope)


def create_keyfile_dict():
    variables_keys = {
        "type": os.environ.get("SHEET_type"),
        "project_id": os.environ.get("SHEET_project_id"),
        "private_key_id": os.environ.get("SHEET_private_key_id"),
        "private_key": os.environ.get("SHEET_private_key").replace('\\n', '\n'),
        "client_email": os.environ.get("SHEET_client_email"),
        "client_id": os.environ.get("SHEET_client_id"),
        "auth_uri": os.environ.get("SHEET_auth_uri"),
        "token_uri": os.environ.get("SHEET_token_uri"),
        "auth_provider_x509_cert_url": os.environ.get("SHEET_auth_provider_x509_cert_url"),
        "client_x509_cert_url": os.environ.get("SHEET_client_x509_cert_url")
    }
    return variables_keys


# print(create_keyfile_dict())
# exit(0)
credentials = ServiceAccountCredentials.from_json_keyfile_dict(create_keyfile_dict(), scope)
client = gspread.authorize(credentials)

# sheet = client.create("NewDatabase1")

# sheet.share('mail2gdek@gmail.com', perm_type='user', role='writer')

# sheet = client.open("NewDatabase1").sheet1
