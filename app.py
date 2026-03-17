from flask import Flask, request, redirect

app = Flask(__name__)

students = {}

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_page(students)


# ---------------- ADD ----------------
@app.route("/add", methods=["POST"])
def add():
    sid = request.form["id"]
    name = request.form["name"]
    course = request.form["course"]

    students[sid] = {"name": name, "course": course}
    return redirect("/")


# ---------------- DELETE ----------------
@app.route("/delete/<sid>")
def delete(sid):
    if sid in students:
        del students[sid]
    return redirect("/")


# ---------------- EDIT ----------------
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
                margin:10px;
                width:90%;
                border-radius:5px;
                border:1px solid #ccc;
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
            <a href="/">Back</a>
        </div>
    </body>
    </html>
    """


# ---------------- UPDATE ----------------
@app.route("/update/<sid>", methods=["POST"])
def update(sid):
    if sid in students:
        students[sid]["name"] = request.form["name"]
        students[sid]["course"] = request.form["course"]
    return redirect("/")


# ---------------- SEARCH ----------------
@app.route("/search")
def search():
    keyword = request.args.get("name", "").lower()

    filtered = {
        sid: data
        for sid, data in students.items()
        if keyword in data["name"].lower()
    }

    return render_page(filtered)


# ---------------- TEMPLATE ----------------
def render_page(data):
    rows = ""
    for sid, student in data.items():
        rows += f"""
        <tr>
            <td>{sid}</td>
            <td>{student['name']}</td>
            <td>{student['course']}</td>
            <td>
                <a class="btn edit" href="/edit/{sid}">Edit</a>
                <a class="btn delete" href="/delete/{sid}">Delete</a>
            </td>
        </tr>
        """

    return f"""
    <html>
    <head>
        <title>Student Dashboard</title>
        <style>
            * {{
                box-sizing: border-box;
                font-family: 'Segoe UI', sans-serif;
            }}

            body {{
                margin: 0;
                background: #f4f6f9;
            }}

            .header {{
                background: linear-gradient(120deg,#4facfe,#00f2fe);
                padding: 20px;
                color: white;
                text-align: center;
                font-size: 28px;
                font-weight: bold;
            }}

            .container {{
                width: 90%;
                max-width: 900px;
                margin: 30px auto;
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            }}

            form {{
                display: flex;
                gap: 10px;
                flex-wrap: wrap;
                margin-bottom: 15px;
            }}

            input {{
                flex: 1;
                padding: 10px;
                border-radius: 6px;
                border: 1px solid #ccc;
            }}

            button {{
                padding: 10px 15px;
                border: none;
                border-radius: 6px;
                background: #4facfe;
                color: white;
                cursor: pointer;
            }}

            button:hover {{
                background: #007bff;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}

            th {{
                background: #4facfe;
                color: white;
                padding: 12px;
            }}

            td {{
                padding: 10px;
                border-bottom: 1px solid #eee;
                text-align: center;
            }}

            tr:hover {{
                background: #f1f7ff;
            }}

            .btn {{
                padding: 6px 10px;
                border-radius: 5px;
                text-decoration: none;
                color: white;
                font-size: 14px;
            }}

            .edit {{
                background: #28a745;
            }}

            .delete {{
                background: #dc3545;
            }}

            .edit:hover {{
                background: #218838;
            }}

            .delete:hover {{
                background: #c82333;
            }}
        </style>
    </head>

    <body>

        <div class="header">🎓 Student Manager</div>

        <div class="container">

            <form action="/add" method="post">
                <input name="id" placeholder="Student ID" required>
                <input name="name" placeholder="Student Name" required>
                <input name="course" placeholder="Course" required>
                <button type="submit">Add</button>
            </form>

            <form action="/search" method="get">
                <input name="name" placeholder="Search student name">
                <button type="submit">Search</button>
            </form>

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


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
