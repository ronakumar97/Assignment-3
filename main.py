from flask import Flask, request, jsonify
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo

app = Flask(__name__)

app.secret_key = "Assignment_3"
client = pymongo.MongoClient("localhost", 27017)

db = client.students

@app.route('/create', methods=['POST'])
def create():
    student_id = request.json['student_id']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    dob = request.json['dob']
    amount_due = request.json['amount_due']

    if request.method == 'POST' and student_id and first_name and last_name and dob and amount_due:
        id = db.user.insert_one({'student_id': student_id, 'first_name': first_name, 'last_name': last_name, 'dob': dob, 'amount_due': amount_due})
        response = jsonify('User added successfully!')
        response.status_code = 200
        return response

    return 'Not Created!!!'

@app.route('/read/<id>')
def read(id):
    students = db.user.find_one({'_id': ObjectId(id)})
    response = dumps(students)
    return response

@app.route('/update/<id>', methods=['PUT'])
def update(id):
    student_id = request.json['student_id']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    dob = request.json['dob']
    amount_due = request.json['amount_due']

    if request.method == 'PUT':
        db.user.update_one({'_id': ObjectId(id)},
                                 {'$set': {'student_id': student_id, 'first_name': first_name, 'last_name': last_name, 'dob': dob, 'amount_due': amount_due}})
        response = jsonify('User updated successfully!')
        response.status_code = 200
        return response

    return 'Not Updated!!!'

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    db.user.delete_one({'_id': ObjectId(id)})
    response = jsonify('User deleted successfully!')
    response.status_code = 200
    return response

@app.route('/read', methods=['GET'])
def read_all():
    students = db.user.find()
    response = dumps(students)
    return response

if __name__ == "__main__":
    app.run(debug=True)