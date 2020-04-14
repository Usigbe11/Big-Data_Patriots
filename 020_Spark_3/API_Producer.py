from time import sleep
from json import dumps
import json
from kafka import KafkaProducer
import requests

producer = KafkaProducer(bootstrap_servers=['localhost:9094'])
body= {"token":"xoxp-846711423270-993711989189-1028701646851-474535ba0f386c760a0f8e6708304938","include_locale":"true","channel":"GV9M2RY92"}
x= requests.get('https://slack.com/api/groups.info',params=body)
result=x.text
result_list= result.splitlines()

print(result)
for x in range(5):
	producer.send('kafka_spark', result.encode('utf-8'))
	print("SUCCESS")	




