import pykafka
import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


#TWITTER API CONFIGURATIONS
access_token = "559516596-yDA9xqOljo4CV32wSnqsx2BXh4RBIRKFxZGSZrPC"
access_token_secret = "zDxePILZitS5tIWBhre0GWqps0FIj9OadX8RZb6w8ZCwz"
consumer_key = "uX0TWqkx0okYEjjqLzxIx6mD6"
consumer_secret = "rzHIs3TMJnADbZNvdGU7LQUo0kPxPISq3RGSLfqcBip39X5END"


#TWITTER API AUTH
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Twitter Stream Listener
class KafkaPushListener(StreamListener):          
	def __init__(self):
		self.client = pykafka.KafkaClient("sandbox-hdp.hortonworks.com:6667")
		self.producer = self.client.topics[bytes("kafka_spark", "ascii")].get_producer()
  
	def on_data(self, data):
		#Producer produces data for consumer
		#Data comes from Twitter
		self.producer.produce(bytes(data, "ascii"))
		return True
                                                                                                                                           
	def on_error(self, status):
		print(status)
		return True

#Twitter Stream Config
twitter_stream = Stream(auth, KafkaPushListener())

#Produce Data that has Corona Virus Keywords (Tweets)
twitter_stream.filter(track=["covid19","coronavirus","Covid-19"])	
