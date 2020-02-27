from flask import Blueprint, jsonify, request, make_response
from .. import db
from .models import Member
from .schemas import MemberSchema

member_api = Blueprint('members', __name__)
member_schema = MemberSchema()
members_schema = MemberSchema(many=True)


@member_api.route('/members', methods=['GET', 'POST'])
def member_view():
    if request.method == 'GET':
        members = Member.query.all()
    elif request.method == 'POST':
        institution = request.get_json()
        members = Member.query.filter_by(institution=institution)

    result = members_schema.dump(members)
    return jsonify({'members': result})


@member_api.route('/add_member', methods=['POST'])
def add_member_view():
    member_data = request.get_json()

    new_member = Member(
        first_name=member_data['firstName'],
        last_name=member_data['lastName'],
        institution=member_data['institution'],
        email_address=member_data['emailAddress']
    )
    db.session.add(new_member)
    db.session.commit()

    response = make_response()
    return response


@member_api.route('/member/<int:member_id>')
def get_member(member_id):
    member = Member.query.get_or_404(member_id)
    result = member_schema.dump(member)

    return jsonify({'member': result})


@member_api.route('/find_members', methods=['POST'])
def find_members():
    search_string = request.get_json()
    print(search_string)
    find = Member.query.get(2)
    result = member_schema.dump(find)
    response = make_response()
    return jsonify(result)
