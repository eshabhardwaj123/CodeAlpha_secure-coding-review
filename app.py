from flask import Flask, request, render_template, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'mysecret'

def get_db_connection():
    conn = sqlite3.connect('users.db')
    return conn

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()

    # 🚩 Vulnerable Query: SQL Injection Risk
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        session['username'] = username
        return "Login successful!"
    else:
        return "Invalid credentials!"

if __name__ == "__main__":
    app.run(debug=True)
