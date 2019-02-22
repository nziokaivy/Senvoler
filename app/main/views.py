from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from flask_login import login_required,current_user
import datetime
from ..requests import get_flight


@main.route('/')
def index():

   
    return render_template('index.html')

@main.route('/search-Now')
def search():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('search.html')


@main.route('/search/flight')
def search_flight():

    flights = get_flight('query')

    return render_template('flight.html',flights=flights)
   