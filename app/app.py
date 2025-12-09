from flask import Flask, jsonify

app = Flask(__name__)

TASKS = [
    {"id": 1, "title": "Купить молоко", "done": False},
    {"id": 2, "title": "Сделать пет-проект на Docker + Nginx", "done": True},
]

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "API работает", "endpoints": ["/tasks"]})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(TASKS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
