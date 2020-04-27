import os
import psycopg2

DATABASE_URL = os.environ['postgres://lbnvhfjrssyoxp:adee998fb724fd6fb676d478eb1e1a309cac276a57ac8fe476a192c8f81d90e2@ec2-54-75-244-161.eu-west-1.compute.amazonaws.com:5432/dfj6k2nuk6jpn3']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')