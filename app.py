from flask import Flask
from flask_migrate import Migrate

from model import db, Production

# initialize the app

app = Flask(__name__)

# configuring the database

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# MIGRATION PROCESS

migrate = Migrate(app, db)
db.init_app(app)

# rOUTES


@app.route("/")
def index():
    return "Hey hallo"


# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
