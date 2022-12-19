# Store this code in 'app.py' file
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import pickle
import numpy as np
import re
import sys 
import os
app = Flask(__name__)
model=pickle.load(open("predictive.pkl",'rb'))

app.secret_key = 'Predictive_maintanance'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['PORT']='3306'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Darshan@1926'
app.config['MYSQL_DB'] = 'predictive_maintenance'

mysql = MySQL(app)

@app.route('/')
@app.route('/Login', methods =['GET', 'POST'])
def login():
    
	msg = ''
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		email = request.form['email']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM login WHERE email = % s AND password = % s', (email, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['email'] = account['email']
			session['password'] = account['password']
			msg = 'Logged in successfully !'
			return render_template('predict.html',msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('Login.html', msg = msg)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    predict=''
    if request.method=='POST':
        unit=int(request.form['unit'])
        cycle=int(request.form['cycle'])
        opset1=float(request.form['opset1'])
        opset2=float(request.form['opset2'])
        sensor2=float(request.form['sensor2'])
        sensor3=float(request.form['sensor3'])
        sensor4=float(request.form['sensor4'])
        sensor7=float(request.form['sensor7'])
        sensor8=float(request.form['sensor8'])
        sensor9=float(request.form['sensor9'])
        sensor11=float(request.form['sensor11'])
        sensor12=float(request.form['sensor12'])
        sensor13=float(request.form['sensor13'])
        sensor15=float(request.form['sensor15'])
        sensor17=float(request.form['sensor17'])
        sensor20=float(request.form['sensor20'])
        sensor21=float(request.form['sensor21'])
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO predictive VALUES ( %d, %d, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f,)', (unit, cycle, opset1, opset2, sensor2, sensor3, sensor4, sensor7, sensor8, sensor9, sensor11, sensor12, sensor13, sensor15, sensor17, sensor20, sensor21 ))
        mysql.connection.commit()
        int_feature=[x for x in request.form.values()]
        final=[np.array(int_feature)]
        prediction=model.predict(final)
        
        return render_template('predict.html', predict=prediction)
    else:
        return render_template('predict.html', predict="sorry somthing went wrong")


@app.route('/logout')
def logout():
	session.pop('Loggedin', None)
	session.pop('email', None)
	session.pop('password', None)
	return redirect(url_for('Login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username'  in request.form and 'email' in request.form and 'password'  in request.form :
		name = request.form['username']
		password = request.form['password']
		email = request.form['email']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM login WHERE username = % s', (name, ))
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', name):
			msg = 'Username must contain only characters and numbers !'
		elif not name or not password or not email:
			msg = 'Please fill out the form !'
		else:
			cursor.execute('INSERT INTO login VALUES ( % s, % s, % s)', (name, email, password, ))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('registration.html', msg = msg)
if __name__ == '__main__':
    app.run(debug=True, port=8000)