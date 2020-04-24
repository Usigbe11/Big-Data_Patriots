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



print("PROGRAM START!!!")
print("PROGRAM START!!!")
print("PROGRAM START!!!")
print("PROGRAM START!!!")

sc= SparkContext()
ssc = StreamingContext(sc, 10)
sqlc= SQLContext(sc)
directKafkaStream = KafkaUtils.createDirectStream(ssc, ["Lufthansa"], {"metadata.broker.list": "localhost:9195"})
lines= directKafkaStream.map(lambda x: x[1])

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
		df.write.format('jdbc').options(url='jdbc:mysql://localhost/BigData',driver='com.mysql.jdbc.Driver',dbtable='Lufthansa',user='fieldemployee',password='Password').mode('append').save()
		df.show()

transform.foreachRDD(build_df)


ssc.start()
ssc.awaitTermination()




