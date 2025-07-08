#Bootstrap Website se acha-acha templates download kar sakte hai for good frontend design

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")
	
@app.route("/about.html")
def about():
	return render_template("about.html")
	
app.run()