from distutils.log import debug
from flask import Flask, render_template, request ,redirect , session

app = Flask(__name__)
app.secret_key = "dogs are so damn cool"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/dog' , methods=['POST'])
def dog():
    session['dogname'] = request.form["name"]
    session['dogbreed'] = request.form["breed"]
    return redirect('/results')

@app.route('/results')
def results():
    print("Getting Dog information")
    return render_template('donzo.html' ,
    dog_name = session['dogname'], 
    dog_breed = session['dogbreed'])

@app.route('/results')
def show_doggies():
    return render_template("donzo.html")

if __name__ == "__main__":
    app.run(debug=True)