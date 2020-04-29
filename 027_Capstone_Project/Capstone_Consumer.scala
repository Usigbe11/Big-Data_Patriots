import org.apache.spark.streaming.StreamingContext._
import org.apache.spark._
import org.apache.spark.streaming._
import org.apache.spark.sql._
import org.apache.spark.sql.types._
import org.apache.spark.streaming.kafka._
import java.util.Properties
import org.apache.spark.sql.SparkSession
import org.apache.spark.SparkConf
import scala.collection.mutable.ListBuffer

object consumer
{	
	def main(args: Array[String]): Unit =
	{
		val linelist: ListBuffer[String] = new ListBuffer[String]();
		val conf = new SparkConf()
		val ss = SparkSession.builder.master("local").appName("Lufthansa").config(conf).getOrCreate()
		import ss.implicits._
		val sc = ss.sparkContext
 		val ssc = new StreamingContext(sc, Seconds(5))
		val sqlContext = new org.apache.spark.sql.SQLContext(sc)
		val dstream = KafkaUtils.createStream(ssc, "localhost:9195", "mygroup" , Map("Lufthansa"-> 1))
		val prop = new Properties()
		prop.setProperty("user", "fieldemployee")
		prop.setProperty("password", "Password")
		val schema = new StructType()
  		.add(StructField("Departure", StringType, false))
  		.add(StructField("D/Time(Local.)", StringType, false))
  		.add(StructField("D/Time(UTC)", StringType, false))
		.add(StructField("Status.", StringType, false))
		.add(StructField("Arrival", StringType, false))
		.add(StructField("D/Time(Local.)", StringType, false))
		.add(StructField("D/Time(UTC.)", StringType, false))
		.add(StructField("Status", StringType, false))
		.add(StructField("Airline_ID", StringType, false))
		.add(StructField("Flight_No", StringType, false))
		.add(StructField("Flight_Status", StringType, false))
		.add(StructField("Service", StringType, false))
		val mappedlines = dstream.foreachRDD{ rdd =>
      		rdd.foreach{record =>
			     var mylist = List(record._2)
			     print(mylist)
			     var myrdd = sc.parallelize(mylist)		     
			     var myrdd2 = myrdd.map{x => Row(x(0),x(1),x(2),x(3),x(4),x(5),x(6),x(7),x(8),x(9),x(10),x(11))}
			     var df = sqlContext.createDataFrame(myrdd2, schema)
			     // Create DF using createDataframe
			     if (df != null)
			     {
				df.write.jdbc(s"jdbc:mysql://localhost:3306/BigData", "Lufthansa", prop)
			     }
			   }
		}
		ssc.start
   		ssc.awaitTermination
	}
}
