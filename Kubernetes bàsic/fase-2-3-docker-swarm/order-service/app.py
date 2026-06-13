from flask import Flask, jsonify
import pymysql
import pika
import os

app = Flask(__name__)

db_host = os.getenv("DB_HOST", "db-orders")
mq_host = os.getenv("MQ_HOST", "message-queue")

@app.route("/order")
def create_order():
    # Guardem la comanda a MySQL
    conn = pymysql.connect(host=db_host, user="root", password="C0ntr@FQrt4_2026!", database="orders")
    cursor = conn.cursor()
    cursor.execute("SELECT 'Comanda creada correctament'")
    conn.commit()

    # Enviem un missatge a RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=mq_host))
    channel = connection.channel()
    channel.queue_declare(queue="orders")
    channel.basic_publish(exchange="", routing_key="orders", body="Nova comanda creada")

    return jsonify({"status": "ok", "message": "Comanda creada i enviada a RabbitMQ"}), 200

app.run(host="0.0.0.0", port=5000)
