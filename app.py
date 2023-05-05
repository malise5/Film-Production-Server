from flask import Flask, make_response, jsonify
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


@app.before_request
def test():
    print("Here we go Again")


@app.route("/")
def index():
    return "Hey hallo"


@app.route("/productions/<string:title>")
def productions(title):
    production = Production.query.filter(Production.title == title).first()
    production_response = {
        "title": production.title,
        "genre": production.genre,
        "director": production.director,
        "budget": production.budget,
        "description": production.description,
        "image": production.image,
        "ongoing": production.ongoing,

    }

    response = make_response(
        jsonify(production_response), 200
    )

    return response


# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
