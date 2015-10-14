from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "Index"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/user/<username>")
def user(username):
	return "User %s" % username

@app.route("/post/80")
def post():
	return "80"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
