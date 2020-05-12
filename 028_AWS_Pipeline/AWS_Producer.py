import boto3
from time import sleep
from json import dumps
import json
import requests

client = boto3.client('kinesis')
shardlist=[]

for x in range(10):
	myheader = {"Authorization": "Bearer d54sj77xdgk6fakuccwgfds7", "Accept": "application/json", "X-Originating-IP": "24.30.40.83"}
	x = requests.get('https://api.lufthansa.com/v1/operations/flightstatus/departures/FRA/2020-05-03T00:00?serviceType=all', headers = myheader)
	responselist = x.json()
	newdict=responselist['FlightStatusResource']
	newdict2= newdict['Flights']
	mylist=newdict2['Flight']
	#print(mylist)


for s in range(10): 
	for i in mylist: 
		shardlist.append(client.put_record(StreamName='Lufthansa', Data=json.dumps(i).encode('utf-8'), PartitionKey='1'))
		print(i)
