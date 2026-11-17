from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json(silent=True) or {}
    # Messages are printed to the console; connect email/DB here if needed.
    print("New message:", data)
    return jsonify(ok=True)


if __name__ == "__main__":
    app.run(debug=True)
