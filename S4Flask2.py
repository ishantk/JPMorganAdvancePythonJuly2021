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

# @app.route("/auth", methods=["POST", "GET"])
@app.route("/auth", methods=["POST"])
def authenticate():
    email = request.form['email']
    password = request.form['password']

    if email == "admin@example.com" and password == "123456":
        return "Welcome Admin"
    else:
        return "Invalid Credentials"

def main():
   app.run()


if __name__ == '__main__':
    main()

