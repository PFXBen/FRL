from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
TRACKS_SPREADSHEET_ID = '1cPp9nfSG5WlJyTK5Avnvh8NqJbQCFNXl6A652sKKrSw'
TRACKS_RANGE_NAME = 'Calendar!B5:I20'
DRIVERS_RANGE_NAME='Drivers!B6:AQ45'

def load():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    tracks_result=service.spreadsheets().values().get(spreadsheetId=TRACKS_SPREADSHEET_ID,range=TRACKS_RANGE_NAME).execute()
    values =tracks_result.get('values',[])

    if not values:
        print('No data found.')
    else:
        for row in values:
            print('%s,%s,%s,%s,%s,%s,%s,%s' %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    
load()
    