#Bootstrap Website se acha-acha templates download kar sakte hai for good frontend design

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://sql12789398:tEkUSPU9G5@sql12.freesqldatabase.com/sql12789398"
db = SQLAlchemy(app)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]

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