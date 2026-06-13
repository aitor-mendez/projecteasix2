from flask import Flask, jsonify
import pymysql
import jwt
import os

app = Flask(__name__)

db_host = os.getenv("DB_HOST", "db-orders")
SECRET = "supersecret"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # Exemple simple
    if email == "a.mendez@sapalomera.cat" and password == "1234":
        return jsonify({"status": "ok", "user_id": 1}), 200
    else:
        return jsonify({"error": "Credencials incorrectes"}), 401

app.run(host="0.0.0.0", port=5000)
