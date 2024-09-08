from confluent_kafka.admin import AdminClient, NewTopic

# Lokales Cluster hört standardmäßig auf den Port 9092
admin = AdminClient({"bootstrap.servers": "localhost:9092"})

# Erstellung eines Topics für einen Temperatursensor mit einer Partition und einer Datenreplizierung
tempSensor1 = NewTopic(
    "tempSensor1",
    num_partitions=1,
    replication_factor=2,
    config={"retention.ms": "86400000"}  # Konfiguration zum Löschen aller Daten, die älter als ein Tag sind
    )

fs = admin.create_topics([tempSensor1])

for topic, f in fs.items():
    try:
        f.result()
        print(f"Topic {topic} wurde erfolgreich erstellt")
    except Exception as e:
        print(f"Error: {topic} konnte nicht erstellt werden: {e}")
