from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

# Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyAfVpJqWSkqSRJUGL_eGOyf95ixMQholy0",
    "authDomain": "yaroni-b899e.firebaseapp.com",
    "projectId": "yaroni-b899e",
    "storageBucket": "yaroni-b899e.appspot.com",
    "messagingSenderId": "1034924839777",
    "appId": "1:1034924839777:web:0854579fc204539a3aeb20",
    "databaseURL": "https://yaroni-b899e-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

# Routes

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = user
            session['email'] = email
            return redirect(url_for('login'))
        except:
            error = "Sign up failed. Please try again."
            return render_template("signup.html", error=error)
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            session['email'] = email
            return redirect(url_for('home'))
        except:
            error = "Login failed. Please try again."
            return render_template("login.html", error=error)
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'post_button' in request.form:
            return redirect(url_for('post'))
        if 'storywall_button' in request.form:
            return redirect(url_for('storywall'))
        if 'candle_button' in request.form:
            return redirect(url_for('light_candle'))
    return render_template('home.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        story_content = request.form['post']
        user_email = session.get('email')
        post_data = {
            'content': story_content,
            'author': user_email
        }
        db.child('posts').push(post_data)
        return redirect(url_for('storywall'))
    return render_template('post.html')

@app.route('/storywall')
def storywall():
    posts = db.child('posts').get().val() or []
    print("Posts fetched:", posts)  # Debugging line
    return render_template('storywall.html', posts=posts)

@app.route('/light_candle', methods=['GET', 'POST'])
def light_candle():
    if request.method == 'POST':
        # Increment candle count
        candle_count = db.child('candle_count').get().val() or 0
        db.child('candle_count').set(candle_count + 1)
        
    # Fetch the current candle count to display
    candle_count = db.child('candle_count').get().val() or 0
    return render_template('candle.html', count=candle_count)

@app.route('/candle')
def candle():
    candle_count = db.child('candle_count').get().val() or 0
    return render_template('candle.html', count=candle_count)

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

