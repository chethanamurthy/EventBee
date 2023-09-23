import requests
import json
import datetime
from tabulate import tabulate
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from googleapiclient import discovery

# Set up the Google Calendar API client
credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=[u'https://www.googleapis.com/auth/calendar'])
calendar_service = build(u'calendar', u'v3', credentials=credentials)


def search_events_by_keyword(keyword):
    try:
        response = requests.get('https://app.ticketmaster.com/discovery/v2/events?apikey=7elxdku9GGG5k8j0Xm8KWdANDgecHMV0&keyword=kids&locale=*&stateCode=CA')
        response.raise_for_status()

        data = response.json()
        events = []

        if '_embedded' in data and 'events' in data['_embedded']:
            event_data = data['_embedded']['events']

            for event in event_data:
                event_id = event['id']
                name = event['name']
                venue = event['_embedded']['venues'][0]['name']
                date = event['dates']['start']['localDate']

                event_info = {
                    'id': event_id,
                    'name': name,
                    'venue': venue,
                    'date': date
                }

                events.append(event_info)

        return events

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []
    
def add_event_to_calendar(event):
    start_date = event['date']
    event_name = event['name']
    event_location = event['venue']

    event_body = {
        'summary': event_name,
        'location': event_location,
        'description': f"Event: {event_name}\nLocation: {event_location}",
        'start': {
            'date': start_date,
            'timeZone': 'America/Los_Angeles',  # Adjust the timezone as needed
        },
        'end': {
            'date': start_date,
            'timeZone': 'America/Los_Angeles',
        },
    }

    # Insert the event into the Google Calendar
    calendar_service.events().insert(calendarId='primary', body=event_body).execute()

def get_unique_venues(events):
    return list(set(event['venue']for event in events))
    #return [event['venue'] for event in events]


if __name__ == '__main__':
    keyword = input("Enter a keyword to search for events: ")
    search_results = search_events_by_keyword(keyword)

    for event in search_results:
        add_event_to_calendar(event)

    print("Events added to your Google Calendar.")