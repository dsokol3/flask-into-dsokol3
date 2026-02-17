Flask Fundamentals Reflection

1. What does the @app.route() decorator actually do?

The @app.route() decorator is a function handler for a specific URL path. It maps URLs to functions. This way Flask knows which function to call for incoming requests.

2. How does Flask know which function to call when a request arrives?

Flask builds a map of URLs and functions when the app starts. When a request comes in, it checks the URL, finds the match in that map, and calls the correct function.

3. What's the difference between route parameters (<name>) and query parameters (?key=value)?

Route parameters are part of the URL itself and get passed into the function directly. Query parameters come after the ?, are optional, and you access them using request.args

4. Why do we need to use request.get_json() for POST requests but request.args.get() for GET query parameters?

POST data is sent in the request body, so you use get_json() to read it.
GET data is in the URL, so you use request.args to get it.

5. What happens if you try to access request.args outside of a request context?

It crashes with an error because Flask only allows request to exist while a request is actually happening. Outside of that, Flask doesn’t know the request