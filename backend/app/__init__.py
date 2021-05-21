from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import yaml

with open("config/config.yaml", 'r') as file:
    try:
        config = yaml.load(file, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        print(exc)

app = Flask(__name__)

app.config['SECRET_KEY'] = config['BACKEND']['SECRET_KEY']

address = "mysql+pymysql://{}:{}@{}:{}/{}".format(
    config['DATABASE']['USER'],
    config['DATABASE']['PASSWORD'],
    config['DATABASE']['HOST'],
    config['DATABASE']['PORT'],
    config['DATABASE']['DB']
)
app.config['SQLALCHEMY_DATABASE_URI'] = address
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

try:
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
except Exception as e:
    print(e)



from app import routes, models
