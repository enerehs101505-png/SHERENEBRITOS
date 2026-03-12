from flask import Flask, request, redirect

app = Flask(__name__)

students = {}

@app.route("/")
def home():
    rows = ""
    for sid, data in students.items():
        rows += f"""
        <tr>
            <td>{sid}</td>
            <td>{data['name']}</td>
            <td>{data['course']}</td>
            <td>
                <a class="edit" href="/edit/{sid}">Edit</a>
                <a class="delete" href="/delete/{sid}">Delete</a>
            </td>
        </tr>
        """

    return f"""
    <html>
    <head>
        <title>Student Dashboard</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(120deg,#4facfe,#00f2fe);
                text-align: center;
                padding: 40px;
            }}
            .container {{
                background: white;
                padding: 30px;
                width: 750px;
                margin: auto;
                border-radius: 10px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            }}
            h1 {{
                color: #333;
            }}
            input {{
                padding: 10px;
                margin: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }}
            button {{
                padding: 10px 15px;
                border: none;
                background: #007BFF;
                color: white;
                border-radius: 5px;
                cursor: pointer;
            }}
            button:hover {{
                background: #0056b3;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 10px;
            }}
            th {{
                background: #007BFF;
                color: white;
            }}
            .edit {{
                color: green;
                margin-right: 10px;
                text-decoration: none;
                font-weight: bold;
            }}
            .delete {{
                color: red;
                text-decoration: none;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Student Manager Dashboard</h1>

            <!-- Add / Update Form -->
            <form action="/add" method="post">
                <input name="id" placeholder="Student ID" required>
                <input name="name" placeholder="Student Name" required>
                <input name="course" placeholder="Course" required>
                <button type="submit">Save</button>
            </form>

            <!-- Search Form -->
            <form action="/search" method="get" style="margin-top: 20px;">
                <input name="name" placeholder="Search student name">
                <button type="submit">Search</button>
            </form>

            <!-- Student Table -->
            <table>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Course</th>
                    <th>Actions</th>
                </tr>
                {rows}
            </table>
        </div>
    </body>
    </html>
    """

@app.route("/add", methods=["POST"])
def add():
    sid = request.form["id"]
    name = request.form["name"]
    course = request.form["course"]
    students[sid] = {"name": name, "course": course}
    return redirect("/")

@app.route("/delete/<sid>")
def delete(sid):
    if sid in students:
        del students[sid]
    return redirect("/")

@app.route("/edit/<sid>")
def edit(sid):
    if sid not in students:
        return redirect("/")
    student = students[sid]
    return f"""
    <html>
    <head>
        <title>Edit Student</title>
        <style>
            body {{
                font-family: Arial;
                background: linear-gradient(120deg,#4facfe,#00f2fe);
                text-align:center;
                padding:50px;
            }}
            .container {{
                background:white;
                padding:30px;
                width:400px;
                margin:auto;
                border-radius:10px;
                box-shadow:0 8px 20px rgba(0,0,0,0.2);
            }}
            input {{
                padding:10px;
                margin:5px;
                border:1px solid #ccc;
                border-radius:5px;
                width:90%;
            }}
            button {{
                padding:10px 15px;
                border:none;
                background:#007BFF;
                color:white;
                border-radius:5px;
                cursor:pointer;
            }}
            button:hover {{
                background:#0056b3;
            }}
            a {{
                display:block;
                margin-top:10px;
                text-decoration:none;
                color:#333;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Edit Student</h2>
            <form action="/update/{sid}" method="post">
                <input name="name" value="{student['name']}" required><br>
                <input name="course" value="{student['course']}" required><br>
                <button type="submit">Update</button>
            </form>
            <a href="/">Back to Dashboard</a>
        </div>
    </body>
    </html>
    """

@app.route("/update/<sid>", methods=["POST"])
def update(sid):
    students[sid]["name"] = request.form["name"]
    students[sid]["course"] = request.form["course"]
    return redirect("/")

@app.route("/search")
def search():
    keyword = request.args.get("name","").lower()
    results = {sid:data for sid,data in students.items() if keyword in data["name"].lower()}
    return results

if __name__ == "__main__":
    app.run(debug=True)
