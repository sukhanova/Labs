"""CRUD-related functions"""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""
    
    movie = Movie(title=title,
                  overview=overview,
                  release_date=release_date,
                  poster_path=poster_path)
    
    db.session.add(movie)
    db.session.commit()

    return movie

def rating(user, movie, score):
    """Create and return a rating."""
    
    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.seesion.commit()

    return rating

if __name__ == '__main__':
    from server import app
    connect_to_db(app)