from flask import Flask, render_template, request , redirect , url_for
from flask import session 
import pyrebase

app = Flask(__name__ , template_folder='templates' , 
static_folder='static')



firebaseConfig = {
	"apiKey": "AIzaSyA6kPll-xOwN7HQ2OcqCJopTX0-oFw2HpE",
  "authDomain": "auth-lab-2920b.firebaseapp.com",
  "projectId": "auth-lab-2920b",
  "storageBucket": "auth-lab-2920b.appspot.com",
  "messagingSenderId": "283895286718",
  "appId": "1:283895286718:web:89e0efdde62406ff3a47ef",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/home' , methods = ['GET' , 'POST'])
def home():
	
	if request.method == 'POST':

		quote = request.form['quotes']

		try:
			session['quotes'].append(quote)
			print(session['quotes'])
			session.modified = True

			return redirect(url_for('thanks'))
		except:
			error = "posting quote failed. Please try again"
			return render_template("home.html" , error = error)
	return render_template("home.html")



@app.route('/display' , methods = ['GET' , 'POST'])
def display():
	quotes = session['quotes']
	return render_template("display.html" , quotes = quotes)


@app.route('/signin' , methods = ['GET' , 'POST'])
def signin():
	if request.method == 'GET':
		return render_template("signin.html")
	else:
		email = request.form['email']
		passowrd = request.form['passowrd']
		try: 
			session['user'] = auth.sign_in_with_email_and_password(email , password)
			session['quotes'] = []
			return redirect(url_for('home'))
		except:
			error = "Log in failed. Please try again."
			return render_template("signin.html" , error = error)
	

@app.route('/' , methods = ['GET' , 'POST'])
def signup():
	if request.method == 'POST':
		email = request.form['email']
		passowrd = request.form['password']
		try:
			session['user'] = auth.create_user_with_email_and_password(email , passowrd)
			session['quotes'] = []
			session['email'] = email
			session['password'] = password
			return redirect(url_for ('signin'))
		except:
			error = "Authentication failed"
			return render_template("signup.html")
	else:
		return render_template("signup.html")


@app.route('/thanks' , methods = ['GET' , 'POST'])
def thanks():
	return render_template("thanks.html")


@app.route('/signout')
def signout():
	session['user'] = None
	auth.current_user = None
	print("User has signed out")
	return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug = True)