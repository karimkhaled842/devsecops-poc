from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def index():
    message = "hello from opsera this a full devsecops project"
    return jsonify(
        {"status": "ok", "message": message, "version": os.getenv("APP_VERSION", "dev")}
    )


@app.route("/health")
def health():
    return jsonify({"healthy": True}), 200


if __name__ == "__main__":
    print("hello from opsera this a full devsecops project")
    app.run(host="0.0.0.0", port=8080, debug=False)  # debug=False is critical
