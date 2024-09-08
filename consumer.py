from confluent_kafka import Consumer

# Config des Consumers "Hadoop":
consumer = Consumer({"bootstrap.servers": "localhost:9092",
                     "group.id": "Flink&Hadoop"})

# Auswahl der Topics deren Daten empfangen werden sollen:
consumer.subscribe(["tempSensor1"])

# Dauerschleife, welche die Daten des ausgewählten Topics ausließt:
while True:
    sensorDaten = consumer.poll(timeout=1.0)

    # Daten sollen nur weitergeleitet werden, wenn neue Daten
    # vom Producer empfangen wurden UND kein Fehler aufgetreten ist:
    if sensorDaten is None:
        continue
    if sensorDaten.error():
        print(f"Consumer error: {sensorDaten.error()}")
        continue
    print(f"Message erhalten: {sensorDaten.value().decode('utf-8')}")

consumer.close()
