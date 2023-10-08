from flask import Flask, render_template, request, redirect, url_for, flash
from seed_database import search_events_by_keyword, get_unique_venues,add_event_to_calendar
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
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
    print(f"In add_to_Calendar: ")
    #try:
    data = request.json
    event_ids = data.get("event_ids", [])
        
    print(f"Event IDs: ",event_ids)

    if not event_ids:
        return jsonify({"message": "No events selected."}), 400   
            
    #print(f"seed_database search_results: ",seed_database.search_results)
    events = seed_database.search_events_by_keyword("kids")
    # Get the events corresponding to the selected event IDs
    selected_events = [event for event in events if event['id'] in event_ids]
    print(f"Selected Event IDs: ",selected_events)
    # Add selected events to the Google Calendar
    for event in selected_events:
        add_event_to_calendar(event)

    return jsonify({"message": "Selected events added to your Google Calendar."}), 200
    #except Exception as e:
        #return jsonify({"message": str(e)}), 500

#User-Login
app.secret_key = 'your_secret_key'  # Change this to a secure secret key
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Simulated user database for demonstration purposes
users = {
    'user1': {'password': 'password1'},
    'user2': {'password': 'password2'},
}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            flash('Logged in successfully', 'success')
            #return redirect(url_for('dashboard'))
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html')

# @app.route('/dashboard')
# @login_required
# def dashboard():
#     return f'Hello, {current_user.id}! This is your dashboard. <a href="/logout">Logout</a>'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))


# @app.route('/dashboard')
# def dashboard():
#     # Retrieve events from the user's Google Calendar
#     calendar_events = seed_database.get_calendar_events()  # Implement this function to fetch calendar events
    
#     return render_template('dashboard.html', calendar_events=calendar_events)

@app.route('/dashboard')
def dashboard():
    google_calendar_events = seed_database.get_calendar_events()
    return render_template('dashboard.html', google_calendar_events=google_calendar_events)




if __name__ == '__main__':
    app.run(debug=True)
