from flask import Flask
import yaml
import os

print (os.getcwd())
with open("backend/config/config.yaml", 'r') as file:
    try:
        config = yaml.load(file, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        print(exc)

app = Flask(__name__)
app.config['SECRET_KEY'] = config['BACKEND']['SECRET_KEY']

from app import routes