import application
from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api=Api(app)
class script(Resource):
    def get(self,written_date,Audience,Topic,Date,Time,Venue):
        application.create(written_date,Audience,Topic,Date,Time,Venue)
        return "DONE"
api.add_resource(script,'/application/<written_date>/<Audience>/<Topic>/<Date>/<Time>/<Venue>')
app.run()
