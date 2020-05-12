import boto3
from time import sleep
from json import dumps
import json
import requests
from pyspark.streaming.kinesis import KinesisUtils, InitialPositionInStream
from pyspark.storagelevel import StorageLevel
from pyspark.streaming import StreamingContext
from pyspark import SparkContext
from pyspark import sql
from pyspark.sql import SQLContext
from pyspark.sql import types
import MySQLdb
import sqlalchemy

client = boto3.client('kinesis')

sc =SparkContext()
ssc = StreamingContext(sc,10)
sqlc = SQLContext(sc)


appName= "Lufthansa_1"
streamName= "Lufthansa"
endpointUrl= "https://kinesis.us-east-2.amazonaws.com"
regionName= "us-east-2"
awsAccessKeyId= "AKIAS5TGRVYITEV4Z4MH"
awsSecretKey= "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"

lines = KinesisUtils.createStream(ssc, appName, streamName, endpointUrl, regionName, InitialPositionInStream.LATEST, 2, StorageLevel.MEMORY_AND_DISK_2, awsAccessKeyId, awsSecretKey)



def transformer(rdd):
	my_obj= json.loads(rdd)
	return (my_obj["Departure"]["AirportCode"],my_obj["Departure"]["ScheduledTimeLocal"]["DateTime"],my_obj["Departure"]["ScheduledTimeUTC"]["DateTime"],my_obj["Departure"]["TimeStatus"]["Code"],my_obj["Arrival"]["AirportCode"],my_obj["Arrival"]["ScheduledTimeLocal"]["DateTime"],my_obj["Arrival"]["ScheduledTimeUTC"]["DateTime"],my_obj["Arrival"]["TimeStatus"]["Code"],my_obj["OperatingCarrier"]["AirlineID"],my_obj["OperatingCarrier"]["FlightNumber"],my_obj["FlightStatus"]["Definition"],my_obj["ServiceType"])

transform= lines.map(transformer)
print(transform)

def build_df(rdd):
	if not rdd.isEmpty():
		global sqlc
		df= sqlc.createDataFrame(rdd, schema= ["Departure","D/Time(Local.)","D/Time(UTC)","Status.","Arrival","D/Time(Local)","D/Time(UTC.)","Status","Airline_ID","Flight_No","Flight_Status","Service"])
		#df.show()
		df.write.format('jdbc').options(url='jdbc:mysql://database-1.cprl59vvy7tz.us-east-2.rds.amazonaws.com:3306/LufthansaTable',driver='com.mysql.cj.jdbc.Driver',dbtable='LufthansaTable',user='fieldemployee',password='Password').mode('append').save()
		df.show()


transform.foreachRDD(build_df)


ssc.start()
ssc.awaitTermination()




