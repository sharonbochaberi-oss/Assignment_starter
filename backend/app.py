from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class Student:
    def __init__(self, id, name, course=None):
        self.id = id
        self.name = name
        self.course = course

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "course": self.course
        }

students = [
    Student(1, "Akida Mwaura", "Software Development"),
    Student(2, "Mike John", "Cyber Security")
]


@app.route('/')
def home():
    return jsonify({
        "message": "Student API is running",
        "endpoints": [
            "GET /students",
            "GET /students/<id>",
            "POST /students",
            "PUT /students/<id>",
            "DELETE /students/<id>"
        ]
    })


@app.route('/students', methods=['GET'])
def get_students():
    return jsonify([s.to_dict() for s in students])

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s.id == id), None)
    if student:
        return jsonify(student.to_dict())
    return jsonify({"error": "Student not found"}), 404

@app.route('/students', methods=['POST'])
def create_student():
    data = request.json

    new_id = students[-1].id + 1 if students else 1
    new_student = Student(new_id, data['name'], data.get('course'))

    students.append(new_student)
    return jsonify(new_student.to_dict()), 201

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    student = next((s for s in students if s.id == id), None)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    student.name = data.get('name', student.name)
    student.course = data.get('course', student.course)

    return jsonify(student.to_dict())

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s.id != id]

    return jsonify({"message": "Deleted"})

if __name__ == '__main__':
    app.run(debug=True)