from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from flask_login import login_required,current_user
import datetime
from ..requests import get_flight
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


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