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

def format_data(data):
    data = data.replace('\n', ' newlinechar ').replace('\r', ' newlinechar ').replace('"', "'")
    return data

def find_parent(pid):
    try:
        sql = "SELECT comment FROM parent_reply WHERE comment_id = '{}' LIMIT 1".format(pid)
        c.execute(sql)
        result = c.fetchone()
        if result != None:
            return result[0]
        else:
            return False
    except Exception as e:
        # print("find_parent", e)
        return False

if __name__ == '__main__':
    create_table()
    row_counter = 0
    paired_row = 0
    with open("/Users/cristigu/Desktop/GithubDesktop/simple-chat/chatdata/reddit_data/{}/RC_{}".format(timeframe.split('-')[0], timeframe), buffering=1000) as f:
        for row in f:
            row_counter += 1
            row = json.loads(row)
            parent_id = row['parent_id']
            body = format_data(row['body'])
            created_utc = row['created_utc']
            score = row['score']
            subreddit = row['subreddit']
            parent_data = find_parent(parent_id)

            if score >= 2:
                existing_comment_score= 
