"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session,redirect, jsonify
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/movies')
def all_movies():
    """View all movies."""
    return render_template('movies.html')

# API
# add your routes here 

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
