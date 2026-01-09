import os                                   # OS utilities for file paths
import gspread                              # Google Sheets library
from oauth2client.service_account import ServiceAccountCredentials  # Service account auth
from googleapiclient.errors import HttpError  # Google API error handling
from gspread.utils import ValueInputOption    # Input option constants


BASE_PATH = os.path.dirname(os.path.abspath(file))  # Directory where this script is located

CSV_FOLDER = os.path.join(BASE_PATH, "csv")             # Path to CSV folder
CSV_PATH = os.path.join(CSV_FOLDER, "myfirstCSV.csv")   # Full path to CSV file

RESOURCE_FOLDER = os.path.join(BASE_PATH, "csv")        # Folder containing credentials JSON

SERVICE_KEY = os.path.join(
    RESOURCE_FOLDER,
    "bionic-comfort-483814-b8-65068774b4ed.json"                    # Service account key file
)

credential = ServiceAccountCredentials.from_json_keyfile_name(
    SERVICE_KEY,
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",  # Sheet read/write
        "https://www.googleapis.com/auth/drive"          # File access & metadata
    ]
)

client = gspread.authorize(credential)                  # Authorize gspread client
sheet_url = "https://docs.google.com/spreadsheets/d/1WXXdYMvaOH1MObphVT445uLJUDH2eo2GFGezfhvbZs8/edit?gid=0#gid=0"
gs_instance = client.open_by_url(sheet_url)              # Open spreadsheet using URL (no Drive scope)
sheet_instance = gs_instance.get_worksheet(0)            # Access first worksheet by index
googlesheet_data_tab0 = sheet_instance.get_all_values()

print(googlesheet_data_tab0)                             # Display retrieved data
new_row_data = [4, "Blue", "BSECE", "1st", 4, "Robot"]
sheet_instance.append_row(new_row_data)