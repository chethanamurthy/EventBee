 # Importing the API Key
from EventBriteAPIKey import key as OAuthKey

# Importing Python web modules
import json, urllib.parse, requests

# Your developer API key
key = OAuthKey

# API Endpoint for user-owned events
eventBrite = "https://www.eventbriteapi.com/v3/users/me/owned_events/"

# API Endpoint: Querying Events in Tempe
eventBriteSearch = "https://www.eventbriteapi.com/v3/events/search/?location.address=Tempe"


def BuildObjects():
    data = requests.get(
        eventBriteSearch,
        headers = { "Authorization": "Bearer " + key,},
        verify = True,).json()

    size = len(data['events'])

    print("\n-------------------")
    print("Total Events {}".format(size))
    print("-------------------\n")

    for index in range(size):
        eventID = data['events'][index]['id']
        title = data['events'][index]['name']['text']
        date  = data['events'][index]['start']['local']
        capacity = data['events'][index]['capacity']
        url = data['events'][index]['url']

        print("# {}\nID: {}\nTitle: {}\nDate:  {}\nCapacity: {}\nURL: {}\n".format(index+1, eventID, title, date, capacity, url))


def main():
    BuildObjects()


if __name__ == '__main__':
    main()