#!/bin/bash
## How to install Sbt

## Update file
sudo apt update

## Create new directory
mkdir opt

## Go in opt
cd opt

## Download Scala
wget https://piccolo.link/sbt-1.3.8.tgz

## Unzip file
tar -zxvf sbt-1.3.8.tgz

## Open txt file of bash profile
sudo gedit .bash_profile

## Set up SBT Home
SBT_HOME=/opt/sbt
export PATH=$PATH:$SBT_HOME/bin

## Source the .bash_profile
source .bash_profile

echo $SBT_HOME

