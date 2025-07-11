from flask import Flask
#flask is the library
#Flask is the function

app = Flask(__name__)
#build the flask app

@app.route("/")
#tells the url - currently / means home
def hello():
	return "Hello World!"
	
@app.route("/page2")
#/ ke baad url pe ye run hoga
@app.route("/dusrapage")
# can add multiple routes too
def page2():
	return "you are in the second page"
	
app.run(debug=True)
#To start the app app.run()
#debug=True refresh the app everytime you make change no need to manual refresh