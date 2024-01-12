from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    # Step 1: Convert the request body into a dictionary
    request_body = request.json
    print("Incoming request with the following body", request_body)

    # Step 2: Add the new todo to the list of todos
    new_todo = {"label": request_body.get("label", ""), "done": False}
    todos.append(new_todo)

    # Step 3: Return the updated list of todos to the frontend
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Step 1: Remove the task from the list of todos by position
    if 0 <= position < len(todos):
        del todos[position]

    # Step 2: Return the updated list of todos in JSON format
    return jsonify(todos)

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
