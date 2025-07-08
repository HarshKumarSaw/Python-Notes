#make static folder for public view
#make template folder for private view

from flask import Flask, render_template
#render_template function html ko python se link karta hai

app = Flask(__name__)

@app.route("/")
def template():
	return render_template("sample.html")
#file location bydefault templates folder ka hota hai

#static folder ka location use karne ke liye static/filename kar sakte hai 
#but instead hum use karte hai {{ url_for('static', filename='fileKAnaam') }} - best practice inline html only not python

#To link python variables to html
@app.route("/variable")
def variable():
	myname = "Harsh"
	return render_template("variable.html", naam = myname)
#To use this variable in html use {{naam}}
	
app.run()