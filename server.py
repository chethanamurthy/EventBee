from flask import Flask, render_template, request
from seed_database import search_events_by_keyword


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

    return render_template('home.html', events=results)


if __name__ == '__main__':
    app.run(debug=True)
