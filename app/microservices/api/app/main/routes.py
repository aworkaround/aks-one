from flask import Blueprint, request, jsonify
from app.models import SimpleTable
from app.main.utils import entry_to_json, new_entry, delete_entry, update_entry
from flask_cors import cross_origin
import random

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({'ReturnCode': 200, 'Message': 'API Server is UP and running.'})

@main.route('/random-entry')
def random_entry():
    id = random.randrange(1000)
    while id > 1000 or id < 1:
        id = random.randrange(1000)
    data = SimpleTable.query.filter_by(id=id).first()
    dt = {
        'username': data.username,
        'email': data.email_id,
        'year_of_birth': data.year_of_birth,
        'age_group': data.age_group
    }
    return jsonify({'ReturnCode': 200, 'Message': dt})

@main.route('/api/entry', methods=['GET', 'POST'])
def entry():
    if request.method == 'GET':
        data = SimpleTable.query.order_by(SimpleTable.id.desc()).all()
        dt = entry_to_json(data)
        return jsonify({
            "ReturnCode": 200,
            "Message": dt
        })
    elif request.method == 'POST':
        data = request.get_json()
        username = data['username']
        email_id = data['email']
        year_of_birth = data['birthyear']
        rc = new_entry(username=username, email_id=email_id, year_of_birth=year_of_birth)
        if rc[0] == 200:
            data = SimpleTable.query.order_by(SimpleTable.id.desc()).all()
            dt = entry_to_json(data)
            return jsonify({
                "ReturnCode": rc[0],
                "Message": dt
            })
        else:
            return jsonify({
                "ReturnCode": rc[0],
                "Message": str(rc[1])
            })

@main.route('/api/delete/<string:email>',  methods=['GET'])
def entry_delete(email):
    rc = delete_entry(email)
    return jsonify({
            "ReturnCode": rc[0],
            "Message": str(rc[1])
        })

@main.route('/api/update',  methods=['POST'])
def entry_update(email):
    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        email_id = data['email']
        year_of_birth = data['birthyear']
        rc = update_entry(email_id=email_id, username=username, year_of_birth=year_of_birth)
        return jsonify({
                "ReturnCode": rc[0],
                "Message": str(rc[1])
            })
    else:
        return jsonify({"ReturnCode": 404, "Message": 'Method not allowed'})