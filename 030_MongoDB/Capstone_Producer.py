from time import sleep
from json import dumps
import json
from kafka import KafkaProducer
import requests

producer = KafkaProducer(bootstrap_servers=['localhost:9195'])

myheader = {"Authorization": "Bearer snbdds8kx7re48fqsj4ubzrn", "Accept": "application/json", "X-Originating-IP": "24.30.40.83"}
x = requests.get('https://api.lufthansa.com/v1/operations/flightstatus/departures/FRA/2020-04-23T00:00?serviceType=all', headers = myheader)

responselist = x.json()
#print(responselist)
newdict=responselist['FlightStatusResource']
newdict2= newdict['Flights']
mylist=newdict2['Flight']

for s in range(0,20): 
	for i in mylist: 
		producer.send('Lufthansa', json.dumps(i).encode('utf-8'))
		print(i)

