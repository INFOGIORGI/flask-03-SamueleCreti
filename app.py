from flask import Flask, render_template

app = Flask(__name__)

lista=(("PatatineS.C", "SC03", 2), ("Philadelphia", "SC04", 3), ("Prosciutto Crudo", "SC05", 2.20))

@app.route("/")
def homepage():
    return render_template("home.html", titolo="Home")

@app.route("/detail")
def detail():
    return render_template("detail.html", titolo="Detail", lista=lista)

@app.route("/scaffale")
def scaffale():
    return render_template("dettagliScaffale.html", titolo="Dettagli Scaffale")

if __name__ == '__main__': 
    app.run(debug=True