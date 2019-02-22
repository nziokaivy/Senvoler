from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    
    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password) :
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Flight:
    def __init__(self, originPlace, inboundDate, cabinClass, children,
                 infants,groupPricing,locale,destinationPlace,outboundDate, country):
        self.originPlace = originPlace
        self.inboundDate = inboundDate
        self.cabinClass = cabinClass
        self.children = children
        self.infants = infants
        self.groupPricing = groupPricing
        self.country = country
        self.locale = locale
        self.destinationPlace = destinationPlace
        self.outboundDate = outboundDate

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.Text)
    destination = db.Column(db.Text)
    date_to = db.Column(db.Text)
    date_from = db.Column(db.Text)
    adults= db.Column(db.Integer)
    infants= db.Column(db.Integer)

    def save_post(self):
        '''
        Function to save a new pitch
        '''
        db.session.add(self)
        db.session.commit()

