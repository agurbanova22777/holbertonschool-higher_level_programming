#!/usr/bin/env python3
"""A simple REST API built with Flask."""


from flask import Flask
from flask import jsonify, request

app = Flask(__name__)
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route("/")
def home():
    """Root endpoint — confirms the API is running."""
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    """Returns a list of all usernames stored in the API."""
    return jsonify(users)

@app.route("/status")
def status():
    """Status endpoint — simple health check."""
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """Returns the full user object for the given username.
    
    <username> is a dynamic segment — Flask captures whatever
    the client puts there and passes it as a function argument.
    """
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/add_user", methods=["POST"])
def add_user():
    """Accepts a POST request with JSON body and adds the user.
    
    Expected JSON: {"username": "john", "name": "John", "age": 30, "city": "New York"}
    """
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username required"}), 400
    
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run()
