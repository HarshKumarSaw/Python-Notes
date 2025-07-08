#Bootstrap Website se acha-acha templates download kar sakte hai for good frontend design

from flask import Flask, render_template

app = Flask(__name__)

#Having same function to different routes
@app.route("/")
@app.route("/index.html")
def home():
	return render_template("index.html")
	
@app.route("/about.html")
def about():
	return render_template("about.html")
	
@app.route("/contact.html")
def contact():
	return render_template("contact.html")
	
@app.route("/post.html")
def post():
	return render_template("post.html")
	
app.run()