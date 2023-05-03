from flask import Flask,render_template
from flask_mysqldb import MySQL
import csv

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Gana@0027'
app.config['MYSQL_DB']='flaskapp'

mysql=MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    # csvdata=csv.reader(open('product.csv'))
    # for row in csvdata:
    #     cur.execute("insert into users (id,name) values(%s,%s)",row)
    #     print(row)

    # mysql.commit()
    # cur.close()
    # print("done")
    cur.execute("select * from users")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template('index.html',data=fetchdata)

if __name__=='__main__':
    app.run(debug = True) 