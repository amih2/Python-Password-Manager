# WARNING
This password manager is written as a hobby project, and is NOT intended for real life use. After this warning if you still use this password manager for real life use, it is on you!

## Python-Password-Manager
CLI based password manager for linux written in python

## General info
* [This password manager uses fernet encryption witch uses on AES]
* [This program is suposed to be run as a root user since database and keys need to be protected against any manipulation other than a master user]
*There is no option to write your own passwords, all passwords are generated with the help of secrets library]
*There is also an option to generate usernames with the help of random_username library]
*Passwords and keys are stored in .json files which are protected with superuser ownership and permissions]

## Installation
``` 
$ git clone https://github.com/amih2/Python-Password-Manager.git
$ cd Python-Password-Manager
$ pip3 install -r requirements.txt --user
```
## Usage
```
$ sudo python3 main.py
```
## Table of contents
* [General info]
* [Technologies]
* [Setup]
