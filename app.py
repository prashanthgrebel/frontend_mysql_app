import os
import mysql.connector 
from flask import Flask, render_template




connection = mysql.connector.connect (host='192.168.1.120',port='3308',database='registration',user='root',password='Pgr@9902#wer')
cursor = connection.cursor()

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/Developer')
def Developer():
  cursor.execute("select * from People where occupation='Developer'")
  value=cursor.fetchall()
  return render_template("occupation.html",data=value,name='Developer')

@app.route('/Engineer')
def Engineer():
  cursor.execute("select * from People where occupation='Engineer'")
  value=cursor.fetchall()
  return render_template("Engineer.html",data=value,name='Engineer')

@app.route('/Leader')
def Leader():
  cursor.execute("select * from People where occupation='Leader'")
  value=cursor.fetchall()
  return render_template("Engineer.html",data=value,name='Leader')

if __name__ == '__main__':
  app.run(port=8000, host='0.0.0.0',debug=True)
