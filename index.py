from flask import Flask, render_template, jsonify
from common import External

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('layout.html')


@app.route("/graph/<length>/", defaults={'gender': 'ALL'})
@app.route("/graph/<length>/<gender>")
def graph(length, gender):
    if length == '10km':
        e = External()
        e.request(External.KEY_10KM, gender)
        e.calculate(5, 16, 0, 30)
    elif length == '21km':
        e = External()
        e.request(External.KEY_21KM, gender)
        e.calculate(5, 24, 1, 5)
    else:
        e = External()
        e.request(External.KEY_42KM, gender)
        e.calculate(10, 20, 2, 40)

    labels = []
    series = []
    for c in e.ranges:
        labels.append(c.label())
        series.append(c.count)

    return jsonify(labels=labels, series=[series])

if __name__ == "__main__":
    app.run(debug=True)
