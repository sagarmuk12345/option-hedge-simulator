from flask import Flask, render_template

app = Flask(__name__)

# Dashboard
@app.route("/")
def dashboard():
    return render_template("index.html")

# Portfolio Page
@app.route("/portfolio")
def portfolio():
    return """
    <h1>Portfolio Page</h1>

    <a href="/">Dashboard</a> |
    <a href="/trades">Trades</a> |
    <a href="/scenario">Scenario</a> |
    <a href="/heatmap">Heat Map</a>

    <hr>

    <p>No positions yet.</p>
    """

# Trades Page
@app.route("/trades")
def trades():
    return render_template("trades.html")

# Scenario Analysis Page
@app.route("/scenario")
def scenario():
    return """
    <h1>Scenario Analysis</h1>

    <a href="/">Dashboard</a> |
    <a href="/portfolio">Portfolio</a> |
    <a href="/trades">Trades</a> |
    <a href="/heatmap">Heat Map</a>

    <hr>

    <p>Future Scenario Engine Coming Soon</p>
    """

# Heat Map Page
@app.route("/heatmap")
def heatmap():
    return """
    <h1>Heat Map</h1>

    <a href="/">Dashboard</a> |
    <a href="/portfolio">Portfolio</a> |
    <a href="/trades">Trades</a> |
    <a href="/scenario">Scenario</a>

    <hr>

    <p>Heat Map Coming Soon</p>
    """

# Start Application
if __name__ == "__main__":
    app.run(debug=True)