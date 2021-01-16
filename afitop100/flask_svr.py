from flask import Flask, request, jsonify
from afitop100 import AFITop100


app = Flask(__name__)

afi = AFITop100()
afi.scrape_afi_list()


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.route("/api/v1/resources/afitop100/all", methods=["GET"])
def api_all():
    return jsonify(afi.afi_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
