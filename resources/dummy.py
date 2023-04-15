from flask_restful import Resource, abort
from flask import request, current_app as app

from controllers.dummyController import Dummy
from resources.authentication import login_required

dummy = Dummy()

class DummyResource(Resource):
    @login_required
    def get(self, user):
        res = dummy.find({ "email": user['email'] })
        app.logger.info(f"{res}")
        return res, 200
    
    def post(self):
        data1 = request.json['data1']
        data2 = request.json['data2']
        app.logger.info(f"Dummy Data Log: {data1, data2}")
        if data1 is None or data2 is None:
            abort(403, message="Invalid Input")
        res = dummy.create({ "data1": data1, "data2": data2 })
        return { "data": res }, 200