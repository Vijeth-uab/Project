from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = 'todo.db'

def create_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

@app.route('/api/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('SELECT * FROM tasks')
        tasks = [{'id': row[0], 'task': row[1]} for row in c.fetchall()]
        conn.close()
        return jsonify(tasks)

    elif request.method == 'POST':
        data = request.json
        task = data.get('task')
        if task:
            conn = sqlite3.connect(DATABASE)
            c = conn.cursor()
            c.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Task added successfully'}), 201
        else:
            return jsonify({'error': 'Invalid data'}), 400

@app.route('/api/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
def task_detail(task_id):
    if request.method == 'PUT':
        data = request.json
        new_task = data.get('task')
        if new_task:
            conn = sqlite3.connect(DATABASE)
            c = conn.cursor()
            c.execute('UPDATE tasks SET task = ? WHERE id = ?', (new_task, task_id))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Task updated successfully'}), 200
        else:
            return jsonify({'error': 'Invalid data'}), 400

    elif request.method == 'DELETE':
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Task deleted successfully'}), 200

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
