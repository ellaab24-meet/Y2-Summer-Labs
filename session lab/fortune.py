from flask import Flask, render_template, request, url_for, session
import random
app = Flask(__name__ , template_folder='templates' , 
static_folder='static')
 
@app.route('/home' , methods = ['GET' , 'POST'])
def home(): 
    if request.method == 'GET':
        return render_template("home.html")
    elif request.method == 'POST':
        birth_month = request.form['birthmonth']
        return (url_for('fortune' , month = birth_month))
    

 
@app.route('/fortune')
def fortune():
    month = request.args.get('month', '')
    month_langth = len(month)
    if month_langth <= len(fortune):
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

    else:
        random_fortune = "your birth month is too long for a fortune"

    return render_template('fortune.html' , fortune = random_fortune)


if __name__ == '__main__': 
    app.run(debug = True)