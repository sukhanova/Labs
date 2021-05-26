"""Script to seed database."""
# This is a module from Python’s standard library. It contains
# code related to working with your computer’s operating system.
import os

# Remember this module from the APIs lab?
# You’ll need this to load the data in data/movies.json.
import json

# choice is a function that takes in a list and returns a random
# element in the list. randint will return a random number within
# a certain range. You’ll use both to generate fake users and ratings.
from random import choice, randint

# We’ll use datetime.strptime to turn a string into a Python datetime obje
from datetime import datetime

# These are all files that you wrote (or will write) — crud.py, model.py, and server.py.
import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# loads data from data/movies.json and saves it to a variable
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())
    
    
#  Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    # set variables title, overview and poster_path to get variables from move DICTIONARY
    # who's key are title, overview, and poster_path in that logical order (can do this
    #because we already used JSON to tranlate the file above! JSON -- key: value)
    title, overview, poster_path = (movie['title'], 
                                    movie['overview'], 
                                    movie['poster_path'])
    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')
    
#print(f"Movie title is: {title}. Overview is {overview}, poster: {poster_path}")
# print(movie[release_date]) use this to see the format of the date
#print(release_date)

#crud is a python file that we already have, and inside that file, we have a function
#called create_movie so both are being assigned to db_new_movies
    db_new_movie = crud.create_movie(title,
                                    overview,
                                    release_date,
                                    poster_path)
    #print(db_new_movie)
    #do we need to use db, explain CRUD
    #CRUD is an idea of abstraction, we put multiple functions within DBs in CRUD so
    #file updates are easier and acessibility is easier

    movies_in_db.append(db_new_movie)

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    # TODO: create a user here

    #we need to use the CRUD.py in order to use the function create_new_user
    new_user = crud.create_user(email, password)

    # TODO: create 10 ratings for the user

    for i in range(10):
        
        random_movie = choice(movies_in_db)
        random_score = randint(1,5)
        
        new_rating = crud.rating(new_user, random_movie, random_score)