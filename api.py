#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

application = Flask(__name__)
api = Api(application)

# @application.route('/')
# def index():
#     return "Index Page"

class TestAPI(Resource):
    def get(self):
        print("GET request called")
        return 'Barebone flask rest api served using docker...'

    def post(self):
        print("POST request called")
        text = request.data.decode('utf-8')
        return text

api.add_resource(TestAPI, '/test')

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8000, debug=True)

