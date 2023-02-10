from flask import Flask , render_template

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorater

@app.route('/home')
def index():
    # -----------Filters--------
    #safe
    #capitalize
    #lower
    #upper
    #title
    #trim
    #striptags

    firstName="John"
    title="This is title text"
    stuff="This is <strong>Bold</strong> Text"

    favouritePizza=["Pepperoni","Cheese Pizza","Hot Dog"]
    return render_template("index.html",
                    first_name=firstName,
                    title=title,
                    stuff=stuff,
                    favourite_pizza=favouritePizza)

# localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)

# Create Custom Error Pages
# Inavalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500