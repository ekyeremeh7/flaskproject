#imported flask's form library
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,ValidationError,SubmitField
from wtforms.validators import DataRequired, Length, Email,EqualTo,required
import phonenumbers


class SubscribeForms(FlaskForm):
    firstname = StringField('Firstname',validators=[DataRequired(),Length(min=2, max=20)])
    lastname =  StringField('Lastname', validators=[Length(min=2, max=20), DataRequired()])
    telephone = StringField('Phone', validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(), Email()])
    submit = SubmitField('Subscribe')
