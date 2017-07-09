#!/bin/sh
#Initializing variables for username and password
username = "usr"
password = "pwd"

#Parse input parameters into defined variables
while getopts "u:p:" opt; do
  case $opt in
    u)
      username="${OPTARG}"
      ;;
    p)
      password="${OPTARG}"
      ;;
  esac
done

#Connecting to MySQL server using user input credentials.
#Creating new database called "hangman" and creating a
# table called "SIMPLEWORDS" in the server
mysql --host=localhost --user=$username --password=$password --execute="create database hangman; use hangman; create table SIMPLEWORDS (words varchar(20));"