import json
from flask import Flask, render_template
import mysql.connector

conn = mysql.connector.connect(user="root",password="root",host="127.0.0.1",database="NaiveCompany",port ='3306')
mycursor = conn.cursor()
query = "SELECT * FROM department"
mycursor.execute(query)
data = mycursor.fetchall()
resp = []
for list_item in (data):
    json_data = {"code":list_item[0],"Name":list_item[1],"Manager":list_item[2]}
    resp.append(json_data)

mycursor.close()
conn.close()

app = Flask(__name__)


@app.route('/')
def main():
    return str(resp)


if __name__ == '__main__':
    app.run()
