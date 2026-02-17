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
    num1 = float(request.args.get("num1", 0))
    num2 = float(request.args.get("num2", 0))
    operation = request.args.get("operation")
    try:
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operation"}), 400
        return jsonify({"result": result, "operation": operation})
    except Exception as e:
        # Log the exception and return an error response
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred during calculation"}), 500
@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    data["echoed"] = True
    return jsonify(data)

@app.route("/status/<int:code>")
def status(code):
    return f"This is a {code} error", code


@app.route('/debug/routes')
def show_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods),
            'path': str(rule)
        })
    return jsonify(routes)


@app.before_request
def log_request():
    current_app.logger.info(f"{request.method} {request.path}")


@app.after_request
def add_header(response):
    response.headers["X-Custom-Header"] = "FlaskRocks"
    return response

@app.teardown_request
def teardown_request(exception=None):
    if exception:
        current_app.logger.error(f"Request ended with exception: {exception}")
    else:
        current_app.logger.info("Request completed successfully")


if __name__ == "__main__":
    app.run(debug=True)
