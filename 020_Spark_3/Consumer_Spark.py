from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark import sql
from pyspark.sql import SQLContext
from pyspark.sql import types
import json
import csv
from json import loads
from flatten_json import flatten
from time import sleep
import pandas as pd


print("PROGRAM START!!!")
print("PROGRAM START!!!")
print("PROGRAM START!!!")
print("PROGRAM START!!!")

sc= SparkContext()
ssc = StreamingContext(sc, 10)
sqlc= SQLContext(sc)
directKafkaStream = KafkaUtils.createDirectStream(ssc, ["kafka_spark"], {"metadata.broker.list": "localhost:9094"})
lines= directKafkaStream.map(lambda x: x[1])

print("LINES START!!!")
print("LINES START!!!")
print("LINES START!!!")
print("LINES START!!!")

def transformer(rdd):
	my_obj= json.loads(rdd)
	return (my_obj["group"]["id"],my_obj["group"]["name"],my_obj["group"]["latest"]["text"],my_obj["group"]["members"],my_obj["group"]["unread_count"])
transform= lines.map(transformer)


def build_df(rdd):
	if not rdd.isEmpty():
		global sqlc
		df= sqlc.createDataFrame(rdd, schema= ["group_id","group_name","group_tasks","members","unread_count"])
		df.show()

transform.foreachRDD(build_df)


ssc.start()
ssc.awaitTermination()

