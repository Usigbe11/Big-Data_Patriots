#!/bin/bash
## How to install Scala 2.8

## Update file
sudo apt update

## Create new directory
mkdir opt

## Go in opt
cd opt

## Download Scala
wget https://scala-lang.org/files/archive/scala-2.8.1.final.tgz?_ga=2.144267061.1615306492.1584022623-1754503928.1583947477

## Unzip file
tar -zxvf scala-2.8.1.final

## Open txt file of bash profile
sudo gedit .bash_profile

## Set up Scala Home
SCALA_HOME=/opt/scala-2.8.1.final
export PATH=$PATH:$SCALA_HOME/bin

## Source the .bash_profile
source .bash_profile

echo $SCALA_HOME

