import time
import pika
import os

mq_host = os.getenv("MQ_HOST", "message_queue")

def connect():
	while True:
		try:
			print("Intentant connectar a RabbitMQ...")
			connection = pika.BlockingConnection(pika.ConnectionParameters(host=mq_host))
			print("Connexió establerta!")
			return connection
		except pika.expections.AMQPConnectionError:
			print("RabbitMQ no està llest. Reintentant en 3s...")
			time.sleep(3)

def start_worker():
	connection = connect()
	channel = connection.channel()
	channel.queue_declare(queue="orders")

	def callback(ch, method, properties, body):
		print(f"[NOTIFICATION] Missatge rebut: {body.decode()}")

	channel.basic_consume(queue="orders", on_message_callback=callback, auto_ack=True)
	print("Esperant missatges")
	channel.start_consuming()

if __name__ == "__main__":
	start_worker()
