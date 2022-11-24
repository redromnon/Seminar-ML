from flask import Flask, render_template, request
app = Flask(__name__)

from model import plotgraph, getinput, plottempgraph

@app.route("/", methods=["GET", "POST"])
def run_model():
    
    if request.method == "POST":
        
        if request.form.get("temp"):
            plottempgraph()
        else:
            getinput(request.form["xinput"], request.form["yinput"])
            plotgraph()

    return render_template("page.html")

if __name__ == "__main__":
    app.run(debug=True)