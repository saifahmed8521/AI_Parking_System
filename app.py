from flask import Flask,render_template

app = Flask(__name__, static_url_path='/static')



@app.route("/")
def MainPage():
    return render_template('index.html')

    

@app.route("/localparking")
def localparking():
    return render_template("local.html")

@app.route("/dtuparking")
def dtuparking():
    return render_template("dtu.html")

if __name__=="__main__":
    app.run(debug=True)
