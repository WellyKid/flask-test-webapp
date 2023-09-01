from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Los angeles',
  'salary': 'USD $100,000'
}, {
  'id': 2,
  'title': 'Control Systems Engineer',
  'location': 'Seattle',
  'salary': 'USD $140,000'
}, {
  'id': 3,
  'title': 'Software Engineer',
  'location': 'Ketchikan',
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
