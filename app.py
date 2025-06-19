from flask import Flask, request, jsonify
import os

app = Flask(__name__)

WHITELIST = ["123456", "abcdef", "mydeviceid"]

@app.route("/check")
def check():
    device_id = request.args.get("id")
    return jsonify(access=device_id in WHITELIST)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
