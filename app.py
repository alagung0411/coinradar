from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')

@app.route('/dashboard')
def dashboard():
    return render_template('AdminPage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Simple placeholder for login logic
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Simple placeholder for signup logic
    return render_template('signup.html')

@app.route('/publish')
def publish():
    return render_template('publish.html')

@app.route('/singlepage')
def singlepage():
    return render_template('singlepage.html')

if __name__ == '__main__':
    app.run(debug=True)
