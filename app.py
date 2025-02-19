from os.path import split

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import telebot
import sqlite3
from telebot import types
from datetime import datetime, timedelta

bot = telebot.TeleBot('7675021564:AAG1vKDuwW-h0fJAFqcokjyhpFNnLiVh8sA')
YOUR_CHAT_ID = '1734603916'
app = Flask(__name__)
connection = sqlite3.connect('my_database.db', check_same_thread=False)
cursor = connection.cursor()
selected_time = None

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE,
    username TEXT,
    number_phone TEXT,
    date_record TEXT,
    time_record TEXT
)
''')

connection.commit()



@app.route("/index")
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/posts")
def posts():
    cursor.execute('SELECT * FROM Users')
    posts = cursor.fetchall()
    print(posts)
    return render_template("posts.html", posts=posts)

@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        title = request.form['title']
        time = request.form['time']
        phone = request.form['number_phone']

        cursor.execute('INSERT INTO Users (username, date_record, number_phone, time_record) VALUES (?, ?, ?, ?)', (title, time.split('T')[0], phone, time.split('T')[1]))

        connection.commit()
        return redirect("/posts")

    else:
        return render_template("create.html")

@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute('DELETE FROM Users WHERE id = ?', (id,))
    connection.commit()
    return redirect("/posts")

if __name__ == '__main__':
    app.run(debug=True)
