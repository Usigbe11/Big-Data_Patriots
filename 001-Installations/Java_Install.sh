#!/bin/bash

## How to install Java 8

## Update file
sudo apt update

## Create new directory
mkdir opt

## Go in opt
cd opt

## Download Java
https://www.oracle.com/java/technologies/javase-jdk8-downloads.html

wget -O jdk-8u221-linux-x64.tar.gz \
-c --content-disposition \
"https://javadl.oracle.com/webapps/download/AutoDL?BundleId=239835_230deb18db3e4014bb8e3e8324f81b43"

## Unzip file
tar -zxvf jdk-8u221-linux-x64.tar.gz

## Open txt file of bash profile
sudo gedit .bash_profile

## Set up the Java_Home

JAVA_HOME=/opt/jdk1.8.0_221
export PATH=$PATH:$JAVA_HOME/bin

echo "Java is created"
