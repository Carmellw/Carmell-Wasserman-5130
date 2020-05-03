from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField , HiddenField , DateTimeField , IntegerField , DecimalField , FloatField , RadioField
from wtforms import Form, SelectMultipleField , BooleanField
from wtforms import TextField, TextAreaField, SelectField
from wtforms import validators, ValidationError
from wtforms.fields.html5 import DateField

from wtforms.validators import DataRequired
from wtforms.validators import InputRequired









class Adataa(FlaskForm):

    date = DateField('Date:' , format='%Y-%m-%d' , validators = [DataRequired])
    country1 = StringField('country1:' , validators = [DataRequired] )
    country2 = StringField('country2:' , validators = [DataRequired] )
    country3 = StringField('country3:' , validators = [DataRequired] )
    country4 = StringField('country4:' , validators = [DataRequired] )
    country5 = StringField('country5:' , validators = [DataRequired] )

    submit = SubmitField('submit')

