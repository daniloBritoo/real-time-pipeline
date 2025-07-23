from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for i in range(10):
    producer.send('meu-topico', f'Mensagem {i}'.encode('utf-8'))
producer.flush()