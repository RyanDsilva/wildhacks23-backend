from flask_restful import Resource, abort
from flask import request, current_app as app

from controllers.sequenceController import Sequence

sequence = Sequence()

class SequenceResource(Resource):
    def get(self):
        res = sequence.find({})
        app.logger.info(f"{res}")
        return res, 200
    
    def post(self):
        key = request.json['key']
        value = request.json['value']
        app.logger.info(f"Dummy Data Log: {key, value}")
        if key is None or value is None:
            abort(403, message="Invalid Input")
        res = sequence.create({ "key": key, "value": value })
        return { "data": res }, 200