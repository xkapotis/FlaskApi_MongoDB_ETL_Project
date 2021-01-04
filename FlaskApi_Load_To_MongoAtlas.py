from flask import Flask, jsonify, json, request, url_for
import pymongo
import json
from pymongo import MongoClient
import dns

cluster = MongoClient(f"mongodb+srv://<username>:<password>@cluster0.uuatc.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test_data"]

app = Flask(__name__)

persons = []

@app.route('/')
def index():
    return "Welcome to Flask Api !!!"

@app.route('/persons', methods=["GET"])
def get():
    return jsonify({
        "Persons": persons
    })


@app.route('/persons', methods=['POST']) 
def post_person():
    content = request.json
    # persons.append(content)    
    collection.insert_one(content)
    return '...'


if __name__ == "__main__":
    app.run(debug=True)

