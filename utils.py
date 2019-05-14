#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Updated on Mon May 13th 2019

@author:    Omer Mustafa
@Credits:   robinreni
"""

import sys
import configparser
import os
import datetime
import pymysql   

class ConfigFileAccessError(Exception):
    pass

def fileexists(CONFIGFILE):
    return(os.path.isfile(CONFIGFILE) )


def get_config():
    
    CONFIGFILE = "./config/config.ini"
    
    Config = configparser.ConfigParser()
    
    config = {}   
    if fileexists(CONFIGFILE):
        Config.read(CONFIGFILE)
        for section in Config.sections():

            subdict = {}
            options = Config.options(section)
            for option in options:
                key = option
                val = Config.get(section,option)
                
                subdict[option] = Config.get(section,option)
                      
            config[section] = subdict
   
    else:
        raise ConfigFileAccessError(CONFIGFILE)

    return config

def query_yes_no(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
            
 
def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i  
                      
def db_connection(host, user, dbname, charset = "utf8mb4"):
   
   
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root',
    passwd='', db='blogbot', charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
    
    # connection = pymysql.connect(host = 'localhost'
    #                             , user = 'blogbot1'
    #                             , password = 'password'
    #                             , db = 'blogbot'
    #                             , charset = charset
    #                             , cursorclass=pymysql.cursors.DictCursor)

    return connection

def db_connectionID(cursor):
    cursor.execute('SELECT connection_id()', (None))
    value = cursor.fetchone()["connection_id()"]
    return(value)

def timestamp_string():
    timestamp_string = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    return(timestamp_string)