from time import sleep
from json import dumps
import json
from kafka import KafkaProducer
import requests

producer = KafkaProducer(bootstrap_servers=['sandbox-hdp.hortonworks.com:6667'])
body= {"Authorization":"xoxp-846711423270-993711989189-1070769478532-251dff61b9df586dc537b97b5f40d736","include_locale":"true","channel":"GV9M2RY92"}
x= requests.get('https://slack.com/api/groups.info',params=body)
result=x.text
result_list= result.splitlines()

print(result)
for x in range(5):
	producer.send('kafka_spark', result.encode('utf-8'))
	print("SUCCESS")	





