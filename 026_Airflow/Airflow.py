import datetime as dt
from time import sleep
from json import dumps
import json
from pyspark.streaming.kafka import KafkaUtils
from kafka import KafkaProducer
from pyspark.streaming import StreamingContext
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark import sql
from pyspark.sql import SQLContext
from pyspark.sql import types
import csv
from json import loads
from flatten_json import flatten
import pandas as pd
import requests
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def producer():
	producer = KafkaProducer(bootstrap_servers=['localhost:9094'])
	body= {"Authorization":"xoxp-846711423270-993711989189-1070769478532-251dff61b9df586dc537b97b5f40d736","include_locale":"true","channel":"GV9M2RY92"}
	x= requests.get('https://slack.com/api/groups.info',params=body)
	result=x.text
	result_list= result.splitlines()

	print (x.text)

	for s in range(10): 
		producer.send('kafka_spark', (x.text).encode('utf-8'))
		print("SUCCESS")


def consumer():
	conf = SparkConf().set("spark.jars", "/home/fielemployee/spark-streaming-kafka-0-8-assembly_2.11-2.4.4.jar")
	sc =SparkContext(conf=conf)
	ssc = StreamingContext(sc,5)
	print("PROGRAM STARTING!!!!!!!!!")
	print("PROGRAM STARTING!!!!!!!!!")

	sqlContext = sql.SQLContext(sc)
	directKafkaStream = KafkaUtils.createDirectStream(ssc, ["kafka_spark"], {"metadata.broker.list":"localhost:9094"})
	lines = directKafkaStream.map(lambda x: x[1])

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



default_args = {
    'owner': 'fieldemployee',
    'start_date': dt.datetime(2020, 4, 22),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}



with DAG('airflow_tutorial_v01',
         default_args=default_args,
         schedule_interval='0 * * * *',
         ) as dag:

    producer = PythonOperator(task_id='producer',
                               python_callable=producer)
    consumer = PythonOperator(task_id='consumer',
                                 python_callable=consumer)


producer >> consumer

