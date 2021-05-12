from flask import Flask, json, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# import data from a json file
with open("scraped_data.json", "r") as file:
    scraped_data = json.load(file)


@app.route("/<crypto>", methods=["GET"])
def get_crypto(crypto):
    # no handling of edge cases
    return jsonify(scraped_data[crypto])

@app.route('/', methods=["GET"])
def home():
	return jsonify(scraped_data)