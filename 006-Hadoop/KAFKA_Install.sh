#!/usr/bin/env bash

## Go in OPT Directory
cd opt

## Create KAFKA Directory
mkdir /home/fieldemployee/opt/kafka

## Go in KAFKA Directory
cd kafka

## Download KAFKA
wget https://www.apache.org/dyn/closer.cgi?path=/kafka/2.3.1/kafka-2.3.1-src.tgz

## Unzip the download
tar -zxvf kafka-2.3.1-src.tgz

## Create a .bash profile
sudo gedit .bash_profile.sh

## Echo $KAFKA_HOME
echo "export KAFKA_HOME=/home/tammy/opt/kafka" >> .bash_profile.sh
