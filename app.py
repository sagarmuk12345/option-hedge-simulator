from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return "<h1>Portfolio Page</h1>"

@app.route("/trades")
def trades():
    return "<h1>Trades Page</h1>"

@app.route("/scenario")
def scenario():
    return "<h1>Scenario Analysis Page</h1>"

@app.route("/heatmap")
def heatmap():
    return "<h1>Heat Map Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)