from flask import Flask, request, jsonify

app = Flask(__name__)

WHITELIST = ["123456", "abcdef", "mydeviceid"]

@app.route("/check")
def check():
    device_id = request.args.get("id")
    if device_id in WHITELIST:
        return jsonify(access=True)
    else:
        return jsonify(access=False)

if __name__ == "__main__":
    app.run()
