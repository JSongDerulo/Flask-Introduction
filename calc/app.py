# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# @app.route('/add')
# def addition():
#     a = request.args["a"]
#     b = request.args["b"]
#     sum = int(a) + int(b)
#     return str(sum)


@app.route('/add')
def addition():
    a = int(request.args["a"])
    b = int(request.args["b"])
    results = add(a,b)

    return str(results)

@app.route('/sub')
def subtraction():
    a = int(request.args["a"])
    b = int(request.args["b"])
    results = sub(a,b)

    return str(results)

@app.route('/mult')
def multiplication():
    a = int(request.args["a"])
    b = int(request.args["b"])
    results = mult(a,b)

    return str(results)

@app.route('/div')
def division():
    a = int(request.args["a"])
    b = int(request.args["b"])
    results = div(a,b)

    return str(results)


operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)