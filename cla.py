import httplib2
import sys

from apiclient.discovery import build
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow

client_id = sys.argv[1]
client_secret = sys.argv[2]

scope = 'https://www.googleapis.com/auth/calendar'

flow = OAuth2WebServerFlow(client_id, client_secret, scope)

def main():

  storage = Storage('credentials.dat')

  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())

  http = httplib2.Http()
  http = credentials.authorize(http)

  service = build('calendar', 'v3', http=http)

  try:

    request = service.events().list(calendarId='primary')
   
    while request != None:
      response = request.execute()
      for event in response.get('items', []):
        
        print repr(event.get('summary', 'NO SUMMARY')) + '\n'
      
      request = service.events().list_next(request, response)

  except AccessTokenRefreshError:
   
    print ('The credentials have been revoked or expired, please re-run'
           'the application to re-authorize')

if __name__ == '__main__':
  main()