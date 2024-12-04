from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os


MONGODB_URI = os.environ["MONGODB_URI"]
DB_NAME = os.environ["DB_NAME"]

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

app.secret_key = bytes.fromhex(os.environ['SECRET_KEY'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')

@app.route('/adminpage')
def dashboard():
    return render_template('AdminPage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Cek apakah user ada dalam database
        user = db.users.find_one({'username': username})

        if user and check_password_hash(user['password'], password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        avatar = request.form.get('avatar')  # Menyimpan avatar jika ada

        # Validasi input
        if not username or not email or not password:
            flash("Please fill in all fields.", 'danger')
            return redirect(url_for('signup'))

        # Hash password sebelum disimpan
        hashed_password = generate_password_hash(password)

        # Simpan data pengguna ke MongoDB
        db.users.insert_one({
            'username': username,
            'email': email,
            'password': hashed_password,
            'avatar': avatar
        })
        
        flash('Signup successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/publish')
def publish():
    return render_template('publish.html')

@app.route('/singlepage')
def singlepage():
    return render_template('singlepage.html')

if __name__ == '__main__':
    app.run(debug=True)
