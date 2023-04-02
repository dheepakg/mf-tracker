# Refer - https://towardsdatascience.com/turn-google-sheets-into-your-own-database-with-python-4aa0b4360ce7

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Connect to Google Sheets
scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("./notes/mf-tracker-gs-creds.json", scope)
client = gspread.authorize(credentials)

sheet = client.create("NewDatabase")

sheet.share('mail2gdek@gmail.com', perm_type='user', role='writer')

sheet = client.open("NewDatabase").sheet1
