from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return ('''<html> <body>
        <h1> Welcome to my photo gallary </h1>
         <p> Our gallary contains photos of food, pets, and outer space!</p> 
        <a href = "/food1"> Go the the first food photo! </a> 
        <a herf = "/food2"> Go to the second food photo! </a>
        <a herf = "/food3"> Go the third food photo! </a> 
        <a herf = "/pet1"> Go to the first pet photo! </a>
        <a herf = "/pet2"> Go to the second pet photo! </a>
        a herf = "/pet3"> Go to the third pet photo! </a>
        <a herf = "/space1"> Go to the first space photo! </a> 
        <a herf = "/space2"> Go to the second space photo! </a>
        <a herf = "/space3"> Go to the third space photo! </a>
        </body> </html>''')

@app.route('/food1')
def food1():
    return('''<html> <body>
        <h1> Welcome to the first food photo! </h1>
            <img src="https://media-cdn.tripadvisor.com/media/photo-s/17/9b/5e/5c/soshi-rolls.jpg">
            <p> I love sushi because it'a tasty and is healthy! <p/>
            <a herf = "/home"> Go to the HomePage <a/>
            <a herf = "/food2"> Go to the second food photo! </a>
        </body> </html>''')

@app.route('/food2')
def food2():
    return('''<html> <body>
        <h1> Welcome to the second food photo! </h1>
        <img src = "https://www.devourdinner.com/wp-content/uploads/2018/04/Teriyaki-Noodles_Devour-Dinner-101.jpg">
        <p> I love noodels because I like making them" </p>
        <a herf = "/home"> Go to home page </a>
        <a herf = "/food3"> Go to the third food photo! </a>
        </body> </html>''')

@app.route('food3')
def food3():
    return('''<html> <body>
        <h1> Welcome to the third food photo! </h1>
        <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjsO76hL4tNLp6ZN_j2m-CyGSpXmf88nzO0Q&s">
        <p> I love ice cream becuse it's refreshing when it's hot out </p>
        <a herf = "/home"> Go to the home page! </a>
        </body> </html>''')

@app.route('pet1')
def pet1():
    return('''<html> <body>
        <h1> Welcome to the first pet photo! </h1>
        <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmI7Mdzsj_yuC0JLzVf6XEtK5A0yOKM9xGUg&s">
        <p> I love golden retrivers because they are really good family dogs! </p>
        <a herf = "/pet2"> Go to the second pet photo! </a>
        <a herf = "/home"> Go to home page </a>
        </body> </html>''')

@app.route('pet2')
def pet2():
    return('''<html> <body>
        <h1> Welcome to the sedond pet photo! </h1>
        <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7v2divJXlMzkB-CdAQigrVbYefdxGaZu3WQ&s">
        <p> I dont like cats </p>
        <a herf = "/pet3"> Go to the second pet photo! </a>
        <a herf = "/home"> Go to the home page </a>
        </body> </html>''')

@app.route('pet3')
def pet3():
    return('''<html> <body> 
        <h1> Welcome to the third pet photo! </h1>
        <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSi0hAfOX_z-D8l5lfsVb629NYn1yKIxntMhQ&s">
        <p> I love duck because they are cute! </p>
        <a herf = "/home"> Go to home page </a>
        </body> </html>''')

@app.route('space1')
def space1():
    return('''<html> <body>
        <h1> Welcome to the first space photo! </h1>
        <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1BUZdB6N1pUTGDlMG7RVgPe1BHBi1YycG8g&s">
        <p> I love our world and the people living in it! </p>
        <a herf = "/home"> Go to home page </a>
        <a herf = "/space2"> Go to the second space photo! </a>
        </body> </html>''')

@app.route('/spce2')
def space2():
    return('''<html> <body>
        <h1> Welcome to the second space photo! </h1>
        <img src = "https://img.freepik.com/free-photo/ultra-detailed-nebula-abstract-wallpaper-4_1562-749.jpg">
        <p> I love the colors in this photos </p>
        <a herf = "/home"> Go to home page </a>
        <a herf = '/space3'> Go to the third space photo! </a>
        </body> </html>''')

@app.route('space3')
def space3():
    retirn('''<html> <body>
        <h1> Welcome to the third space photo! </h1>
        <img src = "https://cdn.mos.cms.futurecdn.net/9UmWCbyxpKaEGXjwFG7dXo-1200-80.jpg">
        <p> I like this photo because it shows the planets around us! </p>
        <a herf = '/home'> Go to home page </a>
        </body> </html>''')



    
if __name__ == '__main__':
    app.run(debug=True)
