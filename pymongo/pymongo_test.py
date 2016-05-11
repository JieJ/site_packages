# -*- coding: utf-8 -*-

"""
pymongo test script

"""
from pymongo import MongoClient


MONGODB_SERVER = '127.0.0.1'    # serve ip address
MONGODB_PORT = 27017            # mongodb port
MONGODB_DB = 'movie'            # db name

client = MongoClient(MONGODB_SERVER, MONGODB_PORT)      # connection
db = client[MONGODB_DB]
collection = db['linux_test']                           # collection name

item = {"name": "jiangjie"}
collection.insert_one(item)
