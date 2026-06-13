from flask import Flask, jsonify
import pymysql
import jwt
import os

app = Flask(__name__)

db_host = os.getenv("DB_HOST", "db-orders")
SECRET = "supersecret"

@app.route("/login")
def login():
	# Validació dummy
	token = jwt.encode({"user": "aitor"}, SECRET, algorithm="HS256")
	return jsonify({"token": token}), 200

app.run(host="0.0.0.0", port=5000)
