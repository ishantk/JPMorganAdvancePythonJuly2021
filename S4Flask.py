"""
    Flask:
        Light Weight Web App Framework
    Documentation:
        https://flask.palletsprojects.com/en/2.0.x/
    Install:
        pip install flask
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index_page():
    text_response = "Welcome to MyApp"
    return text_response

@app.route("/welcome")
def welcome():
    html_response = """
    <html>
        <body>
            <center>
                <h3>Welcome to MyApp with Flask</h3>
                Register Yourself
                <br/>
                Login Here
            </center>
        </body>
    </html>
    """

    return html_response


def main():
   app.run()


if __name__ == '__main__':
    main()

