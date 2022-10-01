from flask import Flask
import sqlite3
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1> Hello  World !! Welcome To Arman Raj... </h1>"


# main driver function
if __name__ == "__main__":

    app.run()
