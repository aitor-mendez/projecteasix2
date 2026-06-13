from flask import Flask, jsonify
import pymysql
import redis
import os

app = Flask(__name__)

db_host = os.getenv("DB_HOST", "db-products")
cache_host = os.getenv("CACHE_HOST", "cache")

# Connexió a Redis
cache = redis.Redis(host=cache_host, port=6379)

@app.route("/products")
def get_products():
	# Primer intentem llegir de la cache
	cached = cache.get("products")
	if cached:
		return jsonify({"source": "cache", "products": cached.decode()}), 200

	# Si no hi ha cache, llegim de MySQL
	conn = pymysql.connect(host=db_host, user="root", password="C0ntr@FQrt4_2026!", database="products")
	cursor = conn.cursor()
	cursor.execute("SELECT 'Producte A', 'Producte B'")
	data = cursor.fetchall()

	# Guardem a la cache
	cache.setex("products", 60, str(data))

	return jsonify({"source": "mysql", "products": str(data)}), 200

app.run(host="0.0.0.0", port=5000)
