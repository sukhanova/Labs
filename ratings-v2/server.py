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

app.secret_key = os.environ['SECRET_KEY']
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
