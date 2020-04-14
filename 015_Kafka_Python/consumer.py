from kafka import KafkaConsumer
from json import loads

f = open('/home/fieldemployee/Kafka_Shakespeare.txt','w')
consumer = KafkaConsumer( 'bigdata', bootstrap_servers=['localhost:9096','localhost:9097','localhost:9098'], auto_offset_reset='earliest')

for message in consumer:
	message = message.value
	f.write(message.decode("utf-8"))


f.close()

