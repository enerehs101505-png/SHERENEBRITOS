from flask import Flask, jsonify, render_template

app = Flask(__name__)

# UI Homepage
@app.route("/")
def home():
    return render_template("index.html")

# API Home
@app.route("/api")
def api():
    return jsonify({
        "message": "Welcome to my Flask API!",
        "student": "SHERENE BRITOS"
    })

# About endpoint
@app.route("/about")
def about():
    return jsonify({
        "project": "Flask API Deployment Activity",
        "developer": "SHERENE BRITOS",
        "status": "Running on Render"
    })

# Hello endpoint
@app.route("/hello/<name>")
def hello(name):
    return jsonify({
        "message": f"Hello {name}! Welcome to my API."
    })

# Extra endpoint
@app.route("/student")
def student():
    return jsonify({
        "name": "Sherene Britos",
        "course": "Information Technology",
        "activity": "Flask API Deployment"
    })

if __name__ == "__main__":
    app.run(debug=True)
