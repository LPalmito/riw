from flask import Flask, render_template, request
from riw.cacm.C_modele_booleen import *
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/search')
def search():
    params = request.args.get("search")
    return params

if __name__ == "__main__":
    app.run()
