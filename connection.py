import io
import snowflake.connector
from flask import jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import matplotlib.pyplot as plt
username = 'suruchi'
password = 'IndLtu$25'
account = 'wc50696.us-east-2.aws'
warehouse = 'compute_wh'
database = 'COVID19_EPIDEMIOLOGICAL_DATA'
schema = 'public'

class Api_data_provider:
    def __init__(self):
        self.conn = snowflake.connector.connect(
            user=username,
            password=password,
            account=account,
            warehouse = warehouse,
            database = database,
            schema = schema
        )
        self.cursor = self.conn.cursor()
    def getData(self , query):
        # Execute SQL queries
        self.cursor.execute(query)
        # Fetch and print results
        data = []
        for row in self.cursor.fetchall():
           data.append(row)
        return data
        
    def close_connection(self):
        self.conn.close()
        
    def data_vis(self,data):
        df = pd.DataFrame(data)
       
       
       
        plt.hist(df)
        
        
        
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
 
        bytes_image.seek(0)
        return bytes_image
     
