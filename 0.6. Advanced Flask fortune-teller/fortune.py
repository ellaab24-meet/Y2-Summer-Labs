from flask import Flask, render_template
import random
app = Flask(__name__ , template_folder='templates' , 
static_folder='static')
 
@app.route('/home')
def home():
    return render_template("home.html")
 
@app.route('/fortune')
def fortune():
    fortunes = [
    "You will have a great day today!" , 
    "You'r most recent dream will come true!" , 
    "Someone will suprise you with a kind gesture!" , 
    "You will be the reason for someone's smile today!" , 
    "Good news is on it's way!" , 
    "If you work hard, it will pay off" , 
    "You will find love in unexpected an place" , 
    "Don't let this oppertunity pass you by!" , 
    "What ever it is you're thinking of doing - don't!" , 
    "Follow you'r heart!"]

    fortNum = random.randint(0, len(fortunes))
    return render_template("fortune.html" , fortune = fortunes[fortNum])
 
app.run(debug = True)