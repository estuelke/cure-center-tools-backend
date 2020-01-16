from flask import Blueprint, jsonify, request, make_response
from .. import db
from .models import Member


member_api = Blueprint('members', __name__)


@member_api.route('/members')
def member_view():
    member_list = [member.serialize for member in Member.query.all()]

    return jsonify({'members': member_list})


@member_api.route('/add_member', methods=['POST'])
def add_member_view():
    member_data = request.get_json()

    new_member = Member(
        first_name=member_data['firstName'],
        last_name=member_data['lastName']
    )
    db.session.add(new_member)
    db.session.commit()

    response = make_response()
    return response
