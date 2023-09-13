# python3 -m pip install flask
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response

app = Flask(__name__)

# curl http://localhost:5000/
@app.route("/")
def home():
    return "Hello world"

@app.route("/ping", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def ping():
    print("=== REQUEST ===")
    print(request)
    print("--- method ---")
    print(request.method)
    print("--- url ---")
    print(request.url)
    print(request.base_url)
    print(request.path)
    print("--- query ---")
    print(request.query_string)
    print(request.args)
    print(request.args.get("foo"))
    print(request.args.to_dict())
    print("--- form ---")
    print(request.form)
    print("--- headers ---")
    print(request.headers)
    print("--- cookies ---")
    print(request.cookies)
    print("--- content-type ---")
    print(request.content_type)
    print("--- data ---")
    print(request.data)
    print("--- json ---")
    # print(request.json)

    result = jsonify({
        "hello": "world"
    })

    response = make_response(result)

    response.headers["Content-Type"] = "application/json"
    response.headers["foo"] = "bar"

    return response


app.run()