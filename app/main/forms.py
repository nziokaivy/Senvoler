from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
from wtforms.validators import Required,Email
from .models import User,Post

class PostForm(FlaskForm):

    origin = StringField(validators=[Required()])
    destination = TextAreaField( validators=[Required()])
    date_to= TextAreaField( validators=[Required()])
    date_from = SubmitField(validators=[Required()])
    adults = TextAreaField(validators=[Required()])
    infants = SubmitField(validators=[Required()])
    submit = SubmitField()
    
   

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
   
    body = TextAreaField('comment', validators=[Required()])
    author = TextAreaField('By', validators=[Required()])
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
    name = StringField("Your Name")
    email = StringField("Email")
    submit= SubmitField('Subscribe')

class PostUpdateForm(FlaskForm):
    title = StringField('Blog title',validators=[Required()])
    body = TextAreaField('Blog', validators=[Required()])
    submit = SubmitField('Publish') 


 id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.Text)
    destination = db.Column(db.Text)
    date_to = db.Column(db.Text)
    date_from = db.Column(db.Text)
    adults= db.Column(db.Integer)
    infants= db.Column(db.Integer)