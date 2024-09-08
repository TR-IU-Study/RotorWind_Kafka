Kafka-Prototyp zur Bereitstellung des Input-Streams und kurzzeitigen Speicherung der Temperaturwerte.

Da keine tatsächlichen Producert und Consumer in diesem Prototyp vorhanden sind, werden Producerseitig zufällige Temperaturwerte erzeugt und an das Kafka-Cluster geschicket, während der Consumer die empfangenen Werte lediglich ausgibt.

Zum starten des Prototypen:
1. Docker Destop Engine aktiviert
2. Zookeeper und Kafka starten über den Terminal-Befehl: 'docker-compose up'
3. Neuste Version von Kafka installieren über den Terminal-Befehl: 'pip install confluent-kafka'
4. Topic erzeugen über den Terminal-Befehl: 'python .\create_topics.py'
5. Consumer starten über den Terminal-Befehl: 'python .\consumer.py'
6. Producer starten über den Terminal-Befehl: 'python .\producer.py'

