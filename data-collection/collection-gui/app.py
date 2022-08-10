from flask import Flask, request, json
from flask_cors import CORS
import collect

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def base():
    try:
        data = request.get_json(force=True)
        sex = data["sex"]
        participant = data["participant"]
        direction = data["direction"]
        run = data["run"]
        collect.collect_data(sex, participant, direction, run)

        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    except Exception as e:
        return json.dumps({'success':False, 'message': e.args[0]}), 400, {'ContentType':'application/json'} 

app.run(host="localhost", port=3000)
