from flask import Flask, render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a Flask Instance
app = Flask(__name__)
app.config["SECRET_KEY"] = "my super secret key"


# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    submit = SubmitField()

    ## ------------ MoreFields ---------------
    # BooleanField  # DateField     # DataTimeField  # FileField    # HiddenField       # MultipleField
    # FieldList     # Floatfield    # FormField      # IntegerField # Passwordfield     # RadioField
    # SelectField   # SelectMultipleField   #SubmitField    # StringField   # TextAreaField      

    ## ------------ Validators --------------
    # DataRequired  # Email # EqualTo   # InputRequired # IPAddress # Length
    # MacAddress    # NumberRange   # Optional  # Regexp    # URL   # AnyOf # NoneOf


# Create a route decorater
@app.route("/")
def index():
    # -----------Filters--------
    # safe  # capitalize    # lower # upper # title # trim  # striptags

    firstName = "John"
    title = "This is title text"
    stuff = "This is <strong>Bold</strong> Text"

    favouritePizza = ["Pepperoni", "Cheese Pizza", "Hot Dog"]

    flash("Welcome To our Website!!!")
    return render_template(
        "index.html",
        first_name=firstName,
        title=title,
        stuff=stuff,
        favourite_pizza=favouritePizza,
    )


# localhost:5000/user/john
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)


# Create Custom Error Pages
# Inavalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

# Create Name Page
@app.route('/name',methods=['GET','POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully!!!")
    return render_template("name.html",name=name,form=form)
