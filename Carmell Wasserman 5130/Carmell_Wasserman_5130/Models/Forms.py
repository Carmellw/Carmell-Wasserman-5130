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

import datetime










class Adataa(FlaskForm):

    date = DateField('Date:' , format='%Y-%m-%d' , validators = [DataRequired()], default=datetime.datetime(2020, 4, 25))
    country1 = SelectField('country1:  ' , validators = [DataRequired()])
    country2 =  SelectField('country2:  ' , validators = [DataRequired()] )
    country3 =  SelectField('country3:  ' , validators = [DataRequired()] )
    country4 = SelectField('country4:  ' , validators = [DataRequired()] )
    country5 = SelectField('country5:  ' , validators = [DataRequired()] )
    cases = SelectField('kind of case:  ' , validators = [DataRequired()] )


    submit = SubmitField('submit')

