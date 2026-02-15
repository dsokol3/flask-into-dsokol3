from flask import Flask, request, current_app, jsonify
from pyexpat.errors import messages

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<p>welcome to Devora's Flask API</p>"


@app.route("/about")
def about():
    var = {"name": "Devora Sokol", "course": "MCON-504 - Backend Development", "semester": "Spring 2025"}
    return jsonify(var)


@app.route("/greet/<name>")
def greet(name):
    return f"<h1>Hi {name}! Welcome to Flask</h1>"


@app.route("/calculate")
def calculate():
    num1 = request.args.get("num1", type=int)
    num2 = request.args.get("num2", type=int)
    operation = request.args.get("operation")
    ans = 0
    if operation == "add":
        ans = num1 + num2
    elif operation == "subtract":
        ans = num1 - num2
    elif operation == "multiply":
        ans = num1 * num2
    elif operation == "divide":
        ans = num1 / num2
    var = {"result": ans, "operation": operation}
    return jsonify(
        {"result": ans,
         "operation": operation}
    )
@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    data["echoed"] = True
    return jsonify(data)
"""
Route 6: Status Code Practice
URL: /status/<int:code>
Method: GET
Response: Return a message with the specified HTTP status code
Example: /status/404 returns "This is a 404 error" with status code 404
Hint: Return a tuple: (message, status_code)
"""
@app.route("/status/<int:code>")
def status(code):
    return f"This is a {code} error", code

if __name__ == "__main__":
    app.run(debug=True)
