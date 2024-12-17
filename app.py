from flask import Flask, render_template

app = Flask(__name__)

tupla=(("PatatineS.C", "SC03", 2), ("Philadelphia", "SC04", 3), ("Prosciutto Crudo", "SC05", 2.20), ("Salame", "SC03", 4))

@app.route("/")
def homepage():
    return render_template("home.html", titolo="Home")

@app.route("/detail")
def detail():
    return render_template("detail.html", titolo="Detail", tupla=tupla)

@app.route("/scaffale/posizione:<nScaffale>")
def scaffale(nScaffale):
    l=[] #creo una lista vuota
    for t in tupla:
        if t[1] == nScaffale:
            l.append(t)
    
    return render_template("dettagliScaffale.html", titolo="Dettagli Scaffale", l=l , nScaffale=nScaffale)

if __name__ == '__main__': 
    app.run(debug=True)