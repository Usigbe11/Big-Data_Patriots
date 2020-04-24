from pyspark.streaming.kafka import KafkaUtils
from pyspark import SparkContext, SparkConf
from pyspark import sql
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext,Row
from pyspark.sql import HiveContext
from pyspark.sql import types
import json
import csv
from json import loads
from time import sleep


sc =SparkContext()
hc = HiveContext(sc)
SparkContext.setSystemProperty("hive.metastore.uris", "thrift://nn1:9083")
ssc = StreamingContext(sc,5)
sqlc = sql.SQLContext(sc)
directKafkaStream = KafkaUtils.createDirectStream(ssc, ["kafka_spark"], {"metadata.broker.list": "sandbox-hdp.hortonworks.com:6667"})
lines= directKafkaStream.map(lambda x: x[1])

#Create Spark session with Hive supported.
appName = "PySpark Hive Example"
master = "sandbox-hdp.hortonworks.com"
ss = SparkSession.builder \
    .appName(appName) \
    .config("spark.sql.warehouse.dir", "/warehouse/tablespace/managed/hive") \
    .getOrCreate()

print("LINES START!!!")
print("LINES START!!!")
print("LINES START!!!")
print("LINES START!!!")


def transformer(rdd):
	my_obj= json.loads(rdd)
	if ("created_at" in my_obj.keys()):		
		return (my_obj["created_at"], my_obj["text"], my_obj["user"]["location"])


transform= lines.map(transformer)

def build_df(rdd):
	if not rdd.isEmpty():
		for x in rdd.collect():      	
			global sqlc
			df=sqlc.createDataFrame(rdd,schema=['Time','Tweet','Location'])
			df.show()
			df.write.saveAsTable(name= 'default.sample_twitter_table',format='parquet',mode='append')
		
transform.foreachRDD(build_df)
transform.pprint()


ssc.start()
ssc.awaitTermination()

