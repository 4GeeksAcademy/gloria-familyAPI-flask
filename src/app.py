from flask import request
from flask import Flask, jsonify
from flask import Flask
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos) # Aquí ese retorna la lista todos como JSON

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)  # Aquí agregamos el contenido a la lista todos
    return jsonify(todos)  # Devuelve la lista actualizada

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)  # Aquí eliminamos el contenido a la lista todos
    return jsonify(todos)  # Devuelve la lista actualizada

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
