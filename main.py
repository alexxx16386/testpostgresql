import os
import psycopg2

DATABASE_URL = os.environ['postgres://scqsmpycssazcb:c5ebcd79218efc56684550121367ab8f04235b54b5fcdeb23fd4cf25c346de96@ec2-54-247-103-43.eu-west-1.compute.amazonaws.com:5432/ddvgha19k56bn2']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
