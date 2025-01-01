import requests
import json
from kafka import KafkaProducer
from time import sleep

url = 'https://api.coinbase.com/v2/prices/btc-usd/spot'
bootstrap_servers = ['localhost:9092']
topics = ['test-topic1', 'test-topic2', 'test-topic3']

producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

while True:
    sleep(2)
    price_data = requests.get(url).json()
    price = float(price_data['data']['amount']) 

    for topic in topics:
        producer.send(topic, value=price_data)

    if price <= 4000:
        producer.send(topics[0], value=price_data)
    elif 4000 < price < 8000:
        producer.send(topics[1], value=price_data)
    else:
        producer.send(topics[2], value=price_data)

    print('Price sent to Kafka:', price_data)

