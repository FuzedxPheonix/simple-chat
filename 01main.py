import sqlite3
import json
from datetime import datetime

# The Reddit comments data timeframe RC_2015-03
timeframe = '2015-03'

sql_transaction = []

connection = sqlite3.connect('{}.db'.format(timeframe))

c = connection.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS parent_reply (parent_id TEXT PRIMARY KEY , comment_id TEXT UNIQUE, parent TEXT, comment TEXT, 
subreddit TEXT, unix TEXT, score INT  )""")

if __name__ == '__main__':
    create_table()
