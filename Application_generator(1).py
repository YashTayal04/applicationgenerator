import application
from flask import Flask, request
app = Flask(__name__)
@app.route('/application_generator', methods=['POST'])
def application_generator() :
    req_data = request.get_json()
    Audience=req_data['audience']
    Topic=req_data['topic']
    Date=req_data['date']
    Time=req_data['time']
    Venue=req_data['venue']
    application.create(Audience,Topic,Date,Time,Venue)
    return "DONE"

app.run()
