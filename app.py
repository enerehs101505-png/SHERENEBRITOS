from flask import Flask, jsonify

app = Flask(__name__)

# Homepage with simple UI
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Flask API Project</title>
        <style>
            body{
                font-family: Arial, sans-serif;
                background: linear-gradient(to right,#4facfe,#00f2fe);
                text-align:center;
                padding:50px;
            }

            .card{
                background:white;
                width:420px;
                margin:auto;
                padding:30px;
                border-radius:10px;
                box-shadow:0px 5px 15px rgba(0,0,0,0.2);
            }

            h1{
                color:#333;
            }

            p{
                color:#555;
            }

            a{
                display:block;
                margin:10px;
                padding:12px;
                text-decoration:none;
                background:#007BFF;
                color:white;
                border-radius:5px;
                font-weight:bold;
            }

            a:hover{
                background:#0056b3;
            }

            footer{
                margin-top:20px;
                color:#777;
            }
        </style>
    </head>

    <body>

    <div class="card">

        <h1>My Flask API</h1>

        <p><strong>Developer:</strong> Sherene Britos</p>

        <p>Welcome to my Flask API Deployment Activity</p>

        <a href="/api">View API Welcome</a>
        <a href="/about">About Project</a>
        <a href="/hello/Guest">Test Hello Endpoint</a>
        <a href="/student">Student Info</a>

        <footer>
        <p>Running on Render</p>
        </footer>

    </div>

    </body>
    </html>
    """

# API welcome route
@app.route("/api")
def api():
    return jsonify({
        "message": "Welcome to my Flask API!",
        "student": "SHERENE BRITOS"
    })

# About route
@app.route("/about")
def about():
    return jsonify({
        "project": "Flask API Deployment Activity",
        "developer": "SHERENE BRITOS",
        "status": "Running on Render"
    })

# Hello route
@app.route("/hello/<name>")
def hello(name):
    return jsonify({
        "message": f"Hello {name}! Welcome to my API."
    })

# Student info route
@app.route("/student")
def student():
    return jsonify({
        "name": "Sherene Britos",
        "course": "Information Technology",
        "activity": "Flask API Deployment"
    })

if __name__ == "__main__":
    app.run(debug=True)
