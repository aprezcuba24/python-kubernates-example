import os
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ["MONGODB_URI"]
mongo = PyMongo(app)
db = mongo.db

print(os.environ["MONGODB_URI"], os.environ["PORT"])


@app.route("/hello-world")
def hello_world():
    return jsonify(data={"data": "Hello World"})


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
    return jsonify(message="Task saved successfully!")


if __name__ == "__main__":
    port = os.environ["PORT"]
    app.run(host="0.0.0.0", port=port, debug=True)
