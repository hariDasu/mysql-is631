from flask import Flask,request,render_template
from flask_bootstrap import Bootstrap
import backend

def createApp():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app=createApp();

@app.route("/")
def test():
    return render_template('test.html')

@app.route("/query1")
def query1():
    results = backend.query1();
    print results
    return results


@app.route("/query2")
def query2():
    results = backend.query2();
    print results
    return results

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

