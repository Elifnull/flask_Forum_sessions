from flask import Flask, redirect, session, render_template, request

app = Flask(__name__)
app.secret_key = "we can do this!"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    session["name"] = request.form["name"]
    session["dojo_location"] = request.form["dojo_location"]
    session["language"] = request.form["program_language"]
    session["comment"] = request.form["comment"]
    session["status"] = request.form["offers"]
    return redirect("/result")

@app.route('/result')
def result():
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)