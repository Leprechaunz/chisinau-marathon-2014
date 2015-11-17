from flask import Flask, render_template, jsonify

from common import External

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('layout.html')


@app.route("/json/<length>")
def json10(length):
    if length == '10km':
        e = External(5, 25)
        e.request(External.KEY_10KM)
        e.calculate(0, 30)
    elif length == '10km':
        e = External(5, 25)
        e.request(External.KEY_21KM)
        e.calculate(1, 00)
    else:
        e = External(10, 21)
        e.request(External.KEY_42KM)
        e.calculate(2, 40)

    return jsonify(ranges=[c.json_dump() for c in e.ranges])


if __name__ == "__main__":
    app.run(debug=True)
