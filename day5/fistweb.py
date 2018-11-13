from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/")
def index():
    return jsonify({"a":"hello world"})

if __name__ == "__main__":
    app.run()
