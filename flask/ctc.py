import csv

# with open('product.txt', 'r') as infile, open('product.csv', 'w') as outfile:
#     stripped = (line.strip() for line in infile)
#     lines = (line.split(",") for line in stripped if line)
#     writer = csv.writer(outfile)
#     writer.writerows(lines)
#     infile.close()
#     outfile.close()

# with open('product.csv', 'r') as outfile:
#     for i in outfile:
#         print(i)
import pandas as pd
from flask import Flask
from flask_mysqldb import MySQL
import mysql.connector
# readinag given csv file
# and creating dataframe
app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Gana@0027'
app.config['MYSQL_DB']='db'

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Gana@0027",
  database="db"
)
dataframe1 = pd.read_csv("product.txt")
  
# storing this datafrcursorame in a csv file
dataframe1.to_csv('product.csv', index = None)
mysql=MySQL(app)
cur = mysql.connection.cursor()
csvdata=csv.reader(open('product.csv'))
for row in csvdata:
    cur.execute("insert into users (id,name) values(%d,%s)",row)
    print(row)

mysql.commit()
cur.close()
print("done")


if __name__=='__main__':
    app.run(debug=True)


