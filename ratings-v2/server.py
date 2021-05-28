"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,redirect)
from model import connect_to_db
import crud
import os
#to throw errors for jinja2 so we will see it instead of error being silent
from jinja2 import StrictUndefined



app = Flask(__name__)
#os.enviorn -> use this to replace the actual key
#don't forget to run source secrets.sh in terminal!!

# app.secret_key = os.environ['SECRET_KEY']
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!

@app.route('/')
def home():
    """View the homepage"""
    return render_template('homepage.html')


@app.route('/movies')
def view_all_movies():
    """View a list of all movies"""
    movies = crud.get_all_movies()
    
    return render_template('all_movies.html',movies=movies)


@app.route('/movies/<movie_id>')   
def display_movie_details(movie_id):
    """Display details by movie id"""
    movie = crud.get_movie_by_id(movie_id)
    
    return render_template('movie_details.html', movie=movie)     

@app.route('/users')
def list_of_users():
    """Display list of all users"""
    users = crud.get_all_users()

    return render_template('all_users.html', users=users)


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user"""
    email = request.form.get('email')
    password = request.form.get('password')
    
    
    user = crud.get_user_by_email(email)
    
    """Check if user exists in a database"""
    if user:
        flash('Username already exist. Please try a new username.')
    else:
        crud.create_user(email,password)
        flash('Account create successfully! Please log in.')

    return redirect('/')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
