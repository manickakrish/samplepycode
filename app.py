from os import name
from flask import Flask,render_template,request,redirect,url_for,session


app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def index():
       return ("Hello World")
                     
if __name__ == "__main__":
  app.run(debug=True)