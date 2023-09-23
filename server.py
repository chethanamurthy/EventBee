from flask import Flask, render_template, request, redirect, url_for, flash
from seed_database import search_events_by_keyword, get_unique_venues,add_event_to_calendar
import seed_database
import os
#from apis import ticketmaster
from flask import Flask, render_template, jsonify, request, session, flash
from model import connect_to_db , db, User, Meeting
from datetime import datetime

app = Flask(__name__)
   

@app.route('/', methods=['GET', 'POST'])
def home():
        if request.method == 'POST':
            search_query = request.form['search']

            # Use the search_results from seed_database.py
            results = search_events_by_keyword(search_query)
        else:
            results = []
        
        venues = get_unique_venues(results)
        print(f"venue list: ", results)

        return render_template('home.html', events=results)

@app.route("/add_to_calendar", methods=["POST"])
def add_to_calendar():
    try:
        data = request.json
        event_ids = data.get("event_ids", [])
        
        if not event_ids:
            return jsonify({"message": "No events selected."}), 400        
        
        # Get the events corresponding to the selected event IDs
        selected_events = [event for event in seed_database.search_results  if event['id'] in event_ids]
        
        # Add selected events to the Google Calendar
        for event in selected_events:
            add_event_to_calendar(event)

        return jsonify({"message": "Selected events added to your Google Calendar."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
