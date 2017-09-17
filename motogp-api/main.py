from flask import Flask, jsonify, make_response, abort, request
from pymongo import MongoClient
from riders import Riders
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the MotoGP REST API"

@app.route('/riders', methods=['GET'])
def get_riders():
    riders = Riders()
    result = riders.get_riders()
    if result:
        return jsonify(result)
    else:
        abort(404)

@app.route('/rider/<rider_id>', methods=['GET'])
def get_rider(rider_id):

    if not str(rider_id).isdigit():
        abort(400)

    riders = Riders()
    result = riders.get_rider(rider_id)
    if result:
        return jsonify(result)
    else:
        abort(404)

@app.route('/v2/riders')
def get_riders_v2():

    year = request.args.get('year')

    if year is None:
        now = datetime.now()
        year = now.year

    classification = request.args.get('classification')

    if classification is None:
        classification = 'MotoGP'

    riders = Riders()
    result = riders.get_riders(year, classification)

    if result:
        return jsonify(result)
    else:
        abort(404)

''' Error Handlers '''

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found", "output": str(error)}), 404)

@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({"error": "Internal Server Error", "output": str(error)}), 500)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({"error": "Bad Request", "output": str(error)}), 400)
