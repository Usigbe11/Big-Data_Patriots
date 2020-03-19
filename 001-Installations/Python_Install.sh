#!/bin/bash
## How to install Python 3.7

## Update file
sudo apt update

## Create new directory
mkdir opt

## Go in opt
cd opt

## Download Python 3.7
wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz

## Unzip file
tar -zxvf Python-3.7.4.tgz

## Enable Python Optimizations
cd Python-3.7.4
./configure --enable-optimizations

##Start the build process
make -j 8

## Install Binaries
sudo make altinstall

## Open bash profile
sudo gedit .bash_profile.sh

## Set up the Python Home
PYTHON_HOME=/opt/Python-3.7.4
export PATH=$PATH:$PYTHON_HOME/bin

## Source the .bash_profile
source .bash_profile

##Check Python version and echo
python3.7 --version
echo $PYTHON_HOME
