from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure=db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = password

class Flight(object):
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
