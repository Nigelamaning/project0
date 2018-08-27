from flask import Flask, render_template, request, session

app = Flask(__name__, template_folder="templates")



@app.route("/")
def index():
	return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
	nombre = request.form.get("nombre")
	return render_template("hello.html", nombre=nombre)