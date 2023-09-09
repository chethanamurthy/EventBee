from flask import Flask, render_template, request, redirect, url_for, flash
#from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from seed_database import search_events_by_keyword, get_unique_venues

app = Flask(__name__)

    # Sample events data
    # events = [
    #     {"name": "Kids Art Class", "date": "2023-09-15"},
    #     {"name": "Children's Storytime", "date": "2023-09-20"},
    #     {"name": "Family Movie Night", "date": "2023-09-25"},
    #     # Add more events here
    # ]

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


if __name__ == '__main__':
    app.run(debug=True)
