from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("checkerboard.html", row=8, column=8, color1='red', color2='black')

@app.route('/<int:x>')
def row(x):
    return render_template("checkerboard.html", row=x, column=8, color1='red', color2='black')

@app.route('/<int:x>/<int:y>')
def row_column(x, y):
    return render_template("checkerboard.html", row=x, column=y, color1='red', color2='black')

@app.route('/<int:x>/<int:y>/<string:one>')
def row_column_one(x, y, one):
    return render_template("checkerboard.html", row=x, column=y, color1=one, color2='black')

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def row_column_two(x, y, one, two):
    return render_template("checkerboard.html", row=x, column=y, color1=one, color2=two)


if __name__=="__main__":
    app.run(debug=True)