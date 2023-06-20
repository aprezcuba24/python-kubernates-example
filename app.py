from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://host.minikube.internal:27017/dev"
mongo = PyMongo(app)
db = mongo.db


@app.route("/")
def get_all_tasks():
    tasks = db.task.find()
    data = []
    for task in tasks:
        item = {"id": str(task["_id"]), "task": task["task"]}
        data.append(item)
    return jsonify(data=data)


@app.route("/", methods=["POST"])
def create_task():
    data = request.get_json(force=True)
    db.task.insert_one({"task": data["task"]})
    return jsonify(message="Task saved successfully")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
