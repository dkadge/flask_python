# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:23:55 2021

@author: Video Disdrometer
"""

from flask import Flask , render_template, jsonify,session,url_for,request,redirect
import mysql.connector
import pymysql
import os
import mutagen

from mutagen.mp3 import MP3
import datetime as dt
#class MyNewClass:
#
#    def method(self, arg):
#        print(self)
#        print(arg)
#        
#my_new_object = MyNewClass()
#my_new_object.method("foo")
#%%
app= Flask(__name__)
app.secret_key='1234554321'
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= "root"
app.config['MYSQL__PASSWORD']= "Dhananjay@13"
app.config['MYSQL_DB']='dj'
#%%
#mydb = MYSQL(app)

#mydb = pymysql.connect(app)
#db=mysql.connector(app)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Dhananjay@13",
  database="dj"
)

mycursor = mydb.cursor(buffered=True)
#The url_for() function is very useful for dynamically building a URL for a specific function.
#%%
@app.route('/loin/',methods=['GET','POST'])
def index():
           
    if request.method == 'POST':
        print('djjjj')
        if 'username' in request.form and 'password' in request.form:
            username=request.form['username']
            password=request.form['password']
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute('SELECT * FROM customers WHERE email=%s AND password=%s',(username,password))
            info=mycursor.fetchone()
            if info is not None:
                if info[2]== username and info[3]==password:
                    session['loginsucess']=True
                    return redirect(url_for('profile'))
            else:
                return redirect(url_for('index'))
        if '/new' in request.form:
            return redirect(url_for('new_user'))
            
    
    print('djj')
    return render_template('login_try.html')
@app.route('/new',methods=['GET','POST'])
def new_user():
    if request.method=='POST':
        if 'one' in request.form and 'two' in request.form and 'three' in request.form:
            username=request.form['one']
            email=request.form['two']
            password=request.form['three']
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute('INSERT INTO customers (name,email,password) VALUES(%s,%s,%s)',(username,email,password))
            mydb.commit()

            return redirect(url_for('index'))
    return render_template('register_try.html')
    
@app.route('/new/profile/')
def profile():
    if session['loginsucess']==True:
#        songs=os.listdir('static/music/')
        songs=[]
        mycursor.execute('SELECT name FROM audiofiles')
        for i in mycursor:
            songs.extend(list(i))
        return render_template('profile_try.html',songs=songs)
    
@app.route('/new/logout')
def logout():
    session.pop('loginsuccess',None)
    return redirect(url_for('index'))
@app.route('/new/update',methods=['GET','POST'])
def update():
    if request.method == 'POST':
        print('djjjj')
        if 'myfile' in request.form:
            myfile1=request.form['myfile']
            print(type(myfile1))
            audio = MP3(os.getcwd()+"\\static\\music\\"+myfile1)
# Contains all the metadata about the mp3 file
            audio_info = audio.info    
            length_secs = int(audio_info.length)
            datetime1=dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute('INSERT INTO audiofiles (name,duration,date) VALUES(%s,%s,%s)',(myfile1,length_secs,datetime1))
            mydb.commit()

            return redirect(url_for('profile'))

    return render_template('update_try.html')
@app.route('/new/delete',methods=['GET','POST'])
def delete():
    songs1=[]
    mycursor.execute('SELECT name FROM audiofiles')
    for i in mycursor:
        songs1.extend(list(i))
        
    if request.method == 'POST':
        print('djjjj')
        if 'song11' in request.form:
            song11=request.form['song11']
            print(type(song11))
            mycursor.execute('DELETE FROM audiofiles WHERE name=%s',(song11,))
            mydb.commit()
            return redirect(url_for('profile'))
            
    
    return render_template('delete_try.html',songs1=songs1)
#@app.route('/')
#def djjjj():
#    return 'hello world'
#@app.route('/hell/')
#def helll():
#    return render_template('profile_try.html')


app.run()


#To release a session variable use pop() method.
#Like Cookie, Session data is stored on client. Session is the time interval when a client logs into a server and logs out of it.