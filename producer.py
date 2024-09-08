from confluent_kafka import Producer

# Import von random und time nur zu Demonstrationszwecken für den Prototypen
import random
import time

producer = Producer({"bootstrap.servers": "localhost:9092"})

# Dauerschleife, die den aktuellen Sensorwert in Form einer Message
# an das in producer.produce übergebene Topic schickt:
while True:

    # Warte einer halben Sekunde
    time.sleep(0.5)

    # Zu Demonstrationszwecken wird hier anstelle eines echten Sensorwerts eine
    # zufällige Temperatur übergeben
    aktuelleTemperatur = random.uniform(25.000, 28.000)
    message = f"{aktuelleTemperatur:.3f}°C"
    print(message)

    # Key für die Nachricht, um die Reihenfolge der Temperaturwerte
    # nachvollziehen zu können, falls irgendwann mehrere Partitionen
    # genutzt werden
    sensor_id = "sensor_1"

    def report(err, msg):
        if err is not None:
            print(f"Error in message: {err}")
        else:
            print(f"Message erfolgreich gesendet {msg.topic()} in partition {msg.partition()}")

    producer.produce("tempSensor1", message.encode("utf-8"), callback=report)
    producer.poll(timeout=1)
