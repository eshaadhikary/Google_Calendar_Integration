#STARTING OF THE CODE
from __future__ import print_function
from ast import Try
from asyncio import events

import datetime
import os.path
from pickle import NONE
from sys import api_version
from xmlrpc.client import NOT_WELLFORMED_ERROR

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#Modifying the scopes
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def main():
    """Showing the basic usage of google calendar api
    Prints the start and name of the next 10 events on the user's calendar 
    """
    creds = NONE
    if os.path.exists('client_secret.json'):
        creds = Credentials.from_authorized_user_file('client_secret.json', SCOPES)
        # if there are no valid credentials let the user sign in 
        if not creds or not creds.valid:
            if creds and cred.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds= flow.run_local_server(port=0)
                # Saving the credentials for the next round
            with open('client_secret.json', 'w') as token:
                token.write(creds.to_json())

        # new_func(creds) 

# def new_func(creds):
    try:
        service = build('calendar', v3, credentials=creds)

            # Calling the calendar api_version
        now= datetime.datetime.utcnow().isoformat()+ 'Z' 
            # Z is the utctime
        print("Getting the upcoming events")
        events_result = service.events().list(calendarId='primary', timeMin=now,maxResults= 10, singleEvents=True,orderBy()=='startTime').execute()   
        events = events_result.get('items', [])

     if not events:
        print('No events upcoming to be found')
        return

    # Printing the names of the upcoming events 
     for event in events:
        start = event['start'].get('datetime', event['start'].get('date'))
        print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' %  error)                  


if __name__=='__main__':
    main()


    # END OF THE CODE 