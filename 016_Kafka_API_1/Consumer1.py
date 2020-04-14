from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer('kafka_spark', bootstrap_servers=['localhost:9096','localhost:9097','localhost:9098'])
for message in consumer:
	print(message.value)
