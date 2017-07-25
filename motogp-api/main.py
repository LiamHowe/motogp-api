from flask import Flask, jsonify, make_response, abort
from pymongo import MongoClient
from riders import Riders

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
