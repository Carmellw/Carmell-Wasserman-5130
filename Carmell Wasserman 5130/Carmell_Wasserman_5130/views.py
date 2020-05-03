"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Carmell_Wasserman_5130 import app
from Carmell_Wasserman_5130.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines

from datetime import datetime
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json 
import requests

import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError

from Carmell_Wasserman_5130.Models.QueryFormStructure import QueryFormStructure 
from Carmell_Wasserman_5130.Models.QueryFormStructure import LoginFormStructure 
from Carmell_Wasserman_5130.Models.QueryFormStructure import UserRegistrationFormStructure 

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from Carmell_Wasserman_5130.Models.plot_service_functions import plot_to_img 
db_Functions = create_LocalDatabaseServiceRoutines() 

from Carmell_Wasserman_5130.Models.QueryFormStructure import Adataa


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )

@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            #return redirect('<were to go if login is good!')
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )




@app.route('/data')
def data():
    """Renders the register page."""
    return render_template(
        'data.html',
        title='Data',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/COVID-19')
def COVID19():

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\covid_19_clean_complete.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')


    """Renders the contact page."""
    return render_template(
        'COVID-19.html',
        title='This is Data Set 1 page',
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message='In this page we will display the datasets we are going to use in order to answer ARE THERE UFOs'
    )


@app.route('/population')
def population():
    """Renders the register page."""
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\population_by_country_2020.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')
    return render_template(
        'population.html',
        title='World Population',
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/Adata')
def Adata():
    form = Adataa(request.form)
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\covid_19_clean_complete.csv'))
    df1 = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\population_by_country_2020.csv'))
    df= df.drop(['Province/State','Lat','Long'],1)
    day=21
    month=3
    country1= 'Israel'
    country2= 'Italy'
    country3= 'China'
    country4= 'Germany'
    country5= 'Canada'
    cases= 'Deaths'
    date= str(month)+'/'+str(day)+'/20'
    df_date= df[(df['Date'])==date]
    df_date= df_date.groupby('Country/Region').sum()
    df1= df1.groupby('Country (or dependency)').sum()
    country1number=df_date.at[country1,cases]/df1.at[country1,'Population (2020)']*10
    country2number=df_date.at[country2,cases]/df1.at[country2,'Population (2020)']*10
    country3number=df_date.at[country3,cases]/df1.at[country3,'Population (2020)']*10
    country4number=df_date.at[country4,cases]/df1.at[country4,'Population (2020)']*10
    country5number=df_date.at[country5,cases]/df1.at[country5,'Population (2020)']*10
    casess = [country1number, country2number,country3number, country4number, country5number]
    index = [country1, country2, country3, country4, country5]
    df = pd.DataFrame({cases: casess}, index=index)
    ax = df.plot.bar(rot=0)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    df.plot(ax = ax , kind = 'bar')
    chart = plot_to_img(fig)
    

    return render_template(
        'Adata.html',
        img_under_construction = '/static/imgs/under_construction.png',
        chart = chart,
        height = "300" ,
        width = "750"

    )
