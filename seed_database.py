import requests
import json
import datetime

from tabulate import tabulate

def search_events_by_keyword(keyword):
    try:
        response = requests.get('https://app.ticketmaster.com/discovery/v2/events?apikey=QhNYM6o1exkzTChcHqRMrN6LGr7BSR7b&keyword=kids&locale=*&stateCode=TX')
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

if __name__ == '__main__':
    keyword = input("Enter a keyword to search for events: ")
    search_results = search_events_by_keyword(keyword)


# def search_events_by_keyword(keyword):
#     API_KEY = 'QhNYM6o1exkzTChcHqRMrN6LGr7BSR7b'
#     endpoint = 'https://app.ticketmaster.com/discovery/v2/events'
    
#     params = {
#         'apikey': API_KEY,
#         'keyword': keyword,
#         'locale': '*',
#         'city': 'Dallas'
#     }

#     try:
#         response = requests.get(endpoint, params=params)
#         response.raise_for_status()

#         data = response.json()
        
#         # Extract and print event data
#         events = []
#         if '_embedded' in data and 'events' in data['_embedded']:
#             event_data = data['_embedded']['events']
#             for event in event_data:
#                 event_id = event['id']
#                 name = event['name']
#                 venue = event['_embedded']['venues'][0]['name']
#                 events.append([event_id, name, venue])

#         if events:
#             # Display events in a table
#             headers = ["Event ID", "Event Name", "Venue"]
#             print(tabulate(events, headers=headers, tablefmt="grid"))
#         else:
#             print("No events found for the given keyword.")

#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")

# if __name__ == '__main__':
#     keyword = input("Enter a keyword to search for events: ")
#     search_results = search_events_by_keyword(keyword)


# Replace 'YOUR_API_KEY' with your actual Ticketmaster API key
# API_KEY = 'QhNYM6o1exkzTChcHqRMrN6LGr7BSR7b'

# Set the base URL for the Ticketmaster API
# BASE_URL = 'https://app.ticketmaster.com/discovery/v2/'

# Define a function to search for events by keyword
# def search_events_by_keyword(keyword):
    # endpoint = 'events.json'
    # params = {
    #     'keyword': keyword,
    #     'apikey': API_KEY
    # }

    # try:
    #     response = requests.get('https://app.ticketmaster.com/discovery/v2/events?apikey=QhNYM6o1exkzTChcHqRMrN6LGr7BSR7b&keyword=kids&locale=*&city=Dallas')
    #     response.raise_for_status()

    #     data = response.json()
    #     print(f'Data Response', data)    
        
    #     attribute_value = data.get("events")
    #     print(f'Data Name', attribute_value)    

    #     # Extract and print event data
    #     if '_embedded' in data:
    #         embeddedd_data = data['_embedded']
    #         if 'events' in embeddedd_data:
    #             event_data = embeddedd_data['events']
    #             for event in event_data:
                    
    #                 event_id = event['id']
    #                 name = event['name']
    #                 print(f'Event ID: ', event_id)
    #                 print(f'Event Name: ', name)
    #                 # date = datetime.datetime.strptime(event_data['dates']['start']['localDate'], '%Y-%m-%d')
    #                 venue = event['_embedded']['venues'][0]['name']

    # except requests.exceptions.RequestException as e:
    #     print(f"Error: {e}")

# if __name__ == '__main__':
#     keyword = input("Enter a keyword to search for events: ")
#     search_events_by_keyword(keyword)
