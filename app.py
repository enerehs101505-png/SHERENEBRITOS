
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to my Flask API!",
        "student": "SHERENE BRITOS"
    })

@app.route("/about")
def about():
    return jsonify({
        "project": "Flask API Deployment Activity",
        "developer": "SHERENEBRITOS",
        "status": "Running on Render"
    })

@app.route("/hello/<name>")
def hello(name):
    return jsonify({
        "message": f"Hello {name}! Welcome to my API."
    })

if __name__ == "__main__":

    app.run(debug=True)        
