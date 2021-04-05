# Put your app in here.

from flask import Flask, request
from operations import *
app = Flask(__name__)

@app.route('/add')
def add_func():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    sum = add(a,b)
    return str(sum)

@app.route('/sub')
def sub_func():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    dif = sub(a,b)
    return str(dif)

@app.route('/mult')
def mult_func():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    prod = mult(a,b)
    return str(prod)

@app.route('/div')
def div_func():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return str(result)

operands = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}
@app.route('/math/<oper>')
def math_fun(oper):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operands[oper](a, b)
    return str(result)


if __name__ == "__main__":
    app.run()
