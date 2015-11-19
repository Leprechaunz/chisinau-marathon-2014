from flask import Flask, render_template, jsonify
from common import External

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('layout.html')


@app.route("/json/<length>")
def json10(length):
    if length == '10km':
        e = External(5, 16)
        e.request(External.KEY_10KM)
        e.calculate(0, 30)
    elif length == '21km':
        e = External(5, 22)
        e.request(External.KEY_21KM)
        e.calculate(1, 00)
    else:
        e = External(10, 21)
        e.request(External.KEY_42KM)
        e.calculate(2, 30)

    labels = []
    series = []
    for c in e.ranges:
        labels.append(c.label())
        series.append(c.count)

    return jsonify(labels=labels, series=[series])


if __name__ == "__main__":
    app.run(debug=True)
