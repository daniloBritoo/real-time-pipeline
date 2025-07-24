from kafka import KafkaProducer
import json, time, random
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    data = {
        "sensor_id": random.randint(1,20),
        "timestamp": time.time(),
        "temperature": round(random.uniform(15,40), 2)
    }
    print(f"enviando: {data}")
    producer.send("temperature_sensor", value=data)
    time.sleep(1)

