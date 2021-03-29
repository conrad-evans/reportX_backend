from flask import Blueprint, request
from src.db import DataBase
from src.middleware import auth


db = DataBase()
intervention_blueprint = Blueprint(
    'intervention', __name__, url_prefix='/intervention')


@intervention_blueprint.route('/')
@auth.loginRequired
def createIntervention():
    data = request.get_json()
    payload = {
        "title": data['title'],
        "content": data['content'],
        "location": {
            "lat": data["location"]["lat"],
            "lon": data["location"]["lon"]
        },
        "video": data["video"],
        "photos": data["photos"]
    }
    data = db.saveIntervention(payload)
    return data
