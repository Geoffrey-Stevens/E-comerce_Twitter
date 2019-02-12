#import flask class from flask module
from flask import Flask
from flask_bootstrap import Bootstrap
#create instance of app variable
app = Flask(__name__)
# once app variable is created import the routes to

#all other variable instances need to come after the app instance
bootstrap = Bootstrap(app)

#load home page
from app import routes
