import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from os import path
import io


def plot_case_1(df , start_date , end_date , kind):
    print("Running from plot_case_1()")
    rd = {}
    start_date_series = df['Start Date']
    ts = pd.to_datetime(start_date_series)
    df['Date'] = ts
    df = df.set_index('Date')
    df1 = df[str(end_date) : str(start_date)]
    series_approving = df1['Approving']
    if series_approving.empty:
        rd['isempty'] = 'empty'
        rd['img'] = ''
    else:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        series_approving.plot(ax=ax,  kind = kind, title = 'Trump Approval Index', figsize = (15, 6), fontsize = 14, style = 'bo-')
        pngImage = io.BytesIO()
        FigureCanvas(fig).print_png(pngImage)
        pngImageB64String = "data:image/png;base64,"
        pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
        rd['isempty'] = ''
        rd['img'] = pngImageB64String
        # return pngImageB64String
    return rd




def plot_to_img(fig):
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String

def covid19_code(date):
    df= df.drop(['Province/State','Lat','Long'],1)
    day=22
    month=3
    country1= 'Israel'
    country2= 'Italy'
    country3= 'China'
    country4= 'Germany'
    country5= 'Canada'
    cases= 'Confirmed'
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

def get_countries_choices(df):
    df1 = df.rename(columns={'Country/Region': 'Country'})
    df1 = df1.groupby('Country').sum()
    l = df1.index
    m = list(zip(l , l))
    return m