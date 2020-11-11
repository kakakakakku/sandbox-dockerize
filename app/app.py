import mysql.connector
import requests

response = requests.get('http://api')

if response.status_code == requests.codes.ok:
    print('✅ API')

conn = mysql.connector.connect(
    host='mysql',
    user='root'
)

if conn.is_connected():
    print('✅ MySQL')
