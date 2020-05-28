from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext
from pyspark import SparkContext
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from pyspark import sql
from pyspark.sql import SQLContext
from pyspark.sql import types
import json
import csv
from json import loads
from time import sleep
import pandas as pd
import pymongo 


print("PROGRAM START!!!")
print("PROGRAM START!!!")
print("PROGRAM START!!!")
print("PROGRAM START!!!")

sc= SparkContext()
ssc = StreamingContext(sc, 10)
sqlc= SQLContext(sc)
directKafkaStream = KafkaUtils.createDirectStream(ssc, ["Lufthansa"], {"metadata.broker.list": "localhost:9195"})
lines= directKafkaStream.map(lambda x: x[1])
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["local"]
mycol = mydb["Lufthansa"]

print("LINES START!!!")
print("LINES START!!!")
print("LINES START!!!")
print("LINES START!!!")

def transformer(rdd):
	my_obj= json.loads(rdd)
	return (my_obj["Departure"]["AirportCode"],my_obj["Departure"]["ScheduledTimeLocal"]["DateTime"],my_obj["Departure"]["ScheduledTimeUTC"]["DateTime"],my_obj["Departure"]["TimeStatus"]["Code"],my_obj["Arrival"]["AirportCode"],my_obj["Arrival"]["ScheduledTimeLocal"]["DateTime"],my_obj["Arrival"]["ScheduledTimeUTC"]["DateTime"],my_obj["Arrival"]["TimeStatus"]["Code"],my_obj["OperatingCarrier"]["AirlineID"],my_obj["OperatingCarrier"]["FlightNumber"],my_obj["FlightStatus"]["Definition"],my_obj["ServiceType"])

transform= lines.map(transformer)
print(transform)

def build_df(rdd):
	if not rdd.isEmpty():
		global sqlc
		df= sqlc.createDataFrame(rdd, schema= ["Departure","D/Time(Local.)","D/Time(UTC)","Status.","Arrival","D/Time(Local)","D/Time(UTC.)","Status","Airline_ID","Flight_No","Flight_Status","Service"])
		pddf= df.toPandas()
		mydict = {'Departure': pddf.iloc[0,0], 'D/Time(Local)': pddf.iloc[0,1], 'D/Time(UTC)': pddf.iloc[0,2], 'Status' :pddf.iloc[0,3], 'Arrival': pddf.iloc[0,4], 'D/Time(Local)' :pddf.iloc[0,5], 'D/Time(UTC)' :pddf.iloc[0,6], 'Status': pddf.iloc[0,7] , 'Airline_ID' : pddf.iloc[0,8],'Flight_No': pddf.iloc[0,9],'Flight_Status': pddf.iloc[0,10], 'Service' : pddf.iloc[0,11] }
		print(mydict)
		x = mycol.insert_one(mydict)
		df.show()

transform.foreachRDD(build_df)


ssc.start()
ssc.awaitTermination()




