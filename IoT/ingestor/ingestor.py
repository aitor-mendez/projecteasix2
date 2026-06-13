import json
import time
import socket
import mysql.connector
from mysql.connector import Error
from paho.mqtt import client as mqtt

connected_to_db = False

while connected_to_db == False:
    try:
        db = mysql.connector.connect(
            host="mariadb",
            user="ingestor",
            password="ingestorpass",
            database="meteorologia"
        )
        print("Connexió a MariaDB OK")
        connected_to_db = True
    except Error:
        print("MariaDB no està llesta, reintentant en 3 segons...")
        time.sleep(3)

def wait_for_port(host, port):
    while True:
        try:
            s = socket.create_connection((host, port), timeout=2)
            s.close()
            return
        except OSError:
            print("MariaDB no respon encara, esperant 3 segons...")
            time.sleep(3)

wait_for_port("mariadb", 3306)

cursor = db.cursor()

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    sql = """
    INSERT INTO dades (
        estacio_id, device_id,
        temperatura, humitat, pressio_atmosferica, velocitat_vent,
        tipus, quality, recorded_at
    ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,NOW())
    """

    values = (
        1,
        data["device_id"],
        data["temperatura"],
        data["humitat"],
        data["pressio"],
        data["vent"],
        "meteo",
        1
    )

    cursor.execute(sql, values)
    db.commit()
    print("Dada inserida:", values)

client = mqtt.Client()
client.connect("mosquitto", 1883)
client.subscribe("meteo/wemos01")
client.on_message = on_message

print("Ingestor escoltant MQTT...")
client.loop_forever()

