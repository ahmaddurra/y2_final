from flask import Flask, render_template, request, redirect, url_for, session
import dataset, random, os


app = Flask(__name__)
app.debug=True
#app.secret_key = urandom(24)

# TODO: set up database



  
@app.route('/')
def homepage():
	return render_template('home.html')
@app.route('/login')
def loginpage():
	return render_template('login.html')
@app.route('/signup')
def signuppage():
	return render_template('signup.html')
@app.route('/about')
def about_page():
	return render_template('about.html')
@app.route('/members')
def members():
	return render_template('member.html')
@app.route('/signedup')
def signedup():
	return render_template('signedup.html')

# TODO: route to /register

# TODO: route to /error

if __name__ == "__main__":
    app.run(port=3000)











