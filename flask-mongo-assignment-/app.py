from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# MongoDB Atlas connection
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["studentDB"]
collection = db["formdata"]

# API Route
@app.route('/api')
def get_data():
    with open('data.json') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/load-data/')
def load_data():

    with open('data.json') as file:
        data = json.load(file)

    collection.insert_many(data)

    return "Data inserted into MongoDB"

# Homepage with form
@app.route('/')
def form():
    return render_template("form.html")

# Form submission
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        # Insert into MongoDB
        collection.insert_one({
            "name": name,
            "email": email
        })

        # Update data.json
        with open("data.json", "r") as file:
            data = json.load(file)

        # Add new record
        data.append({
            "name": name,
            "email": email
        })

        # Write back to file
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        return redirect(url_for('success'))

    except Exception as e:
        return str(e)

# Success page
@app.route('/success')
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run(debug=True)