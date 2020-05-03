"""
This script runs the Carmell_Wasserman_5130 application using a development server.
"""

from os import environ
from Carmell_Wasserman_5130 import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.config['SECRET_KEY']="IHATEMYLIFE"
    app.run(HOST, PORT)
