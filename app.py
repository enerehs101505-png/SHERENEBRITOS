from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Home page with UI
@app.route("/")
def home():
    return render_template("index.html")

# API: Home info
@app.route("/api")
def api_home():
    return jsonify({
        "message": "Welcome to my Flask API!",
        "student": "SHERENE BRITOS"
    })

# API: About
@app.route("/about")
def about():
    return jsonify({
        "project": "Flask API Deployment Activity",
        "developer": "SHERENE BRITOS",
        "status": "Running on Render"
    })

# API: Greeting
@app.route("/hello/<name>")
def hello(name):
    return jsonify({
        "message": f"Hello {name}! Welcome to my API."
    })

if __name__ == "__main__":
    app.run(debug=True)
