from kafka import KafkaConsumer
import json
import subprocess

bootstrap_servers = ['localhost:9092']
topics = ['topic1', 'topic2', 'topic3']
hdfs_paths = ['/input/bit_coin_topic1.txt', '/input/bit_coin_topic2.txt', '/input/bit_coin_topic3.txt']

def append_to_hdfs(data, hdfs_path):
    command = ['hadoop', 'fs', '-appendToFile', '-', hdfs_path]
    subprocess.run(command, input=data.encode('utf-8'), check=True)

try:
    consumers = []
    for topic, hdfs_path in zip(topics, hdfs_paths):
        consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers,
                                 value_deserializer=lambda x: json.loads(x.decode('utf-8')))
        consumers.append((consumer, hdfs_path))

    for consumer, _ in consumers:
        consumer.subscribe(topics)

    for consumer, hdfs_path in consumers:
        for message in consumer:
            price_data = json.dumps(message.value)
            append_to_hdfs(price_data + '\n', hdfs_path)
            print(f'Received and appended to ({hdfs_path}):', price_data)


