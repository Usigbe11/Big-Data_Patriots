from time import sleep
from json import dumps
import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9096','localhost:9097','localhost:9098'])
f = open('/home/fieldemployee/shakespeare.txt', 'r')
line_list = f.readlines()

for e in range(len(line_list)):
	producer.send('bigdata',json.dumps(line_list[e]).encode('utf-8'))
	sleep(1)
	


