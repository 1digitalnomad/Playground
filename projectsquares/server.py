from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def play():
    return render_template("index.html", Document="My Squares", header="My Squares")

@app.route('/play/<num>')
def playx(num):
    return render_template("plays.html", Document="My Squares", header="My Squares", times=int(num))

@app.route('/play/<num>/<color>')
def playcolor(num,color):
    return render_template("playscolor.html", Document="My Squares", header="My Squares", times=int(num),color=color)

if __name__=="__main__":
    app.run(debug=True)
