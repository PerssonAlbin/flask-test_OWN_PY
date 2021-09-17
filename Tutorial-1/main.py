from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello world! <h1>TEST<h1>"

@app.route("/<name>")
def user(name):
	return "Hello {0}!".format(name)

@app.route("/admin")
def admin():
	return redirect(url_for("home"))

if __name__ == "__main__":
	app.run()
