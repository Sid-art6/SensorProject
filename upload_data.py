from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri = 'mongodb+srv://sid:12345@cluster0.sjbcjrv.mongodb.net/?'

# Create a new client and connect to server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME = 'project'
COLLECTION_NAME = 'waferfault'

df = pd.read_csv('C:\Users\SIDDHANT\Downloads\SensoryProject\notebooks\wafer_23012020_041211.csv')

df=df.drop('Unnamed: 0' , axis = 1)

json_record =list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)