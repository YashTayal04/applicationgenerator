import application
from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app)
@app.route('/application_generator', methods=['POST'])
def application_generator():
    print('hello')
    req_data = request.get_json()
    audience=req_data['audience']
    topic=req_data['topic']
    date=req_data["date"]
    time=req_data["time"]
    venue=req_data['venue']
    print(audience, topic, date, time, venue)
    application.create(audience, topic, date, time, venue)
    return "DONE"

app.run(debug=True)
