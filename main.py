from flask import Flask, render_template, request
app = Flask(__name__)

from model import plotgraph, getinput

@app.route("/", methods=["GET", "POST"])
def hello_world():

    if request.method == "POST":
        getinput(request.form["xinput"], request.form["yinput"])
        plotgraph()

    return render_template("page.html")

if __name__ == "__main__":
    app.run(debug=True)