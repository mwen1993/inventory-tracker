from flask import Flask
import configparser

credential = configparser.ConfigParser()
credential.read('credential.conf')
app = Flask(__name__)
app.config['SECRET_KEY'] = credential.get('Credential', 'secret_key')

from app import routes
