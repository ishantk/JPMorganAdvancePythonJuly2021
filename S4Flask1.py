"""
    Flask:
        Light Weight Web App Framework
    Documentation:
        https://flask.palletsprojects.com/en/2.0.x/
    Install:
        pip install flask
"""
from flask import *

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/loginstudent")
def login_student():
    return render_template("login-student.html")

@app.route("/loginteacher")
def login_teacher():
    return render_template("login-teacher.html")

@app.route("/admin")
def admin():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/<type>")
def application_routes(type):
    print("type is:", type)
    if type == "student":
        return redirect(url_for('login_student'))
    elif type == "teacher":
        return redirect(url_for('login_teacher')) # -> url_for -> use function name
    elif type == "admin":
        return redirect(url_for('admin'))
    else:
        return "INVALID OR BAD REQUEST"


def main():
   app.run()


if __name__ == '__main__':
    main()

