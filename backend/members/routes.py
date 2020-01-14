from flask import Blueprint, jsonify, request
from backend import db
from backend.members.models import Member


member_api = Blueprint('members', __name__)


@member_api.route('/members')
def member_view():
    member_list = Member.query.all()
    members = []

    for member in member_list:
        members.append({
            'first_name': member.first_name,
            'last_name': member.last_name})
    return jsonify({'members': members})


@member_api.route('/add_member', methods=['POST'])
def add_member_view():
    member_data = request.get_json()

    new_member = Member(
        first_name=member_data['first_name'],
        last_name=member_data['last_name']
    )

    db.session.add(new_member)
    db.session.commit()

    return 'Done', 201
