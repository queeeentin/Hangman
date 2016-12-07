#!/bin/bash
timeout=5

pip install -U pip
sleep $timeout
sudo pip install distribute
sleep $timeout
sudo pip install nose
sleep $timeout
sudo pip install virtualenv



