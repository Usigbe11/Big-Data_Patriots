#!/bin/bash

## How to install Hadoop 3.1.3

## Update file
sudo apt update

## Create new directory
mkdir opt

## Go in opt
cd opt

## Download Hadoop
wget http://apache.mirrors.hoobly.com/hadoop/common/current/hadoop-3.1.3.tar.gz

## Unzip the file
tar -zxvf hadoop-3.1.3.tar.gz

## Open txt file of bash profile
sudo gedit .bash_profile.sh

## Set up Hadoop Home
echo "export HADOOP_HOME=/home/tammy/opt/hadoop" >> .bash_profile.sh
echo "export HADOOP_INSTALL=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_MAPRED_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_COMMON_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_HDFS_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export YARN_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native" >> .bash_profile.sh
echo "export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin" >> .bash_profile.sh

##Source bash profile
source .bash_profile.sh

## Set up the Hadoop Configuration files
cd hadoop/etc/hadoop

## Edit hadoop-env.sh
sudo gedit hadoop-env.sh
echo "export JAVA_HOME=/usr/lib/jvm/java-11-oracle" >> hadoop-env.sh

## Edit core-site.xml
sudo gedit core-site.xml
echo "<configuration>
<property>
  <name>fs.default.name</name>
    <value>hdfs://localhost:9000</value>
</property>
</configuration>" >> core-site.xml

## Edit hdfs-site.xml
sudo gedit hdfs-site.xml
echo "<configuration>
<property>
 <name>dfs.replication</name>
 <value>1</value>
</property>
<property>
  <name>dfs.name.dir</name>
    <value>file:///home/hadoop/hadoopdata/hdfs/namenode</value>
</property>

<property>
  <name>dfs.data.dir</name>
    <value>file:///home/hadoop/hadoopdata/hdfs/datanode</value>
</property>
configuration>" >> hdfs-site.xml

## Edit mapred-site.xml
sudo gedit mapred-site.xml
echo "<configuration>
 <property>
  <name>mapreduce.framework.name</name>
   <value>yarn</value>
 </property>
</configuration>" >> mapred-site.xml

## Edit yarn-site.xml
sudo gedit yarn-site.xml
echo "<configuration>
 <property>
  <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
 </property>
</configuration>" >> yarn-site.xml

## Format HDFS Namenode
hdfs namenode -format

## Start Hadoop Cluster
cd $HADOOP_HOME/sbin/
./start-dfs.sh

## Run start-hdfs.sh
./start-hdfs.sh

## Run start-yarn.sh
./start-yarn.sh

## To upload a file from the home directory into HDFS
hdfs dfs -put "filename" /"destination directory"

## To confirm file upload
hdfs dfs -ls /"destination directory"


