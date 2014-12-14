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
    return render_template('mysqlZips.html')

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


@app.route("/query3")
def query3():
    results = backend.query3();
    print results
    return results

@app.route("/query4")
def query4():
    results = backend.query4();
    print results
    return results

@app.route("/mysqlEmps")
def emps():
    return render_template('mysqlEmps.html')

@app.route("/empQuery1")
def empQuery1():
    results=backend.empQuery1()
    print results
    return results

@app.route("/empQuery2")
def empQuery2():
    results=backend.empQuery2()
    print results
    return results


@app.route("/empQuery3")
def empQuery3():
    results=backend.empQuery3()
    print results
    return results


@app.route("/empQuery4")
def empQuery4():
    results=backend.empQuery4()
    print results
    return results

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

