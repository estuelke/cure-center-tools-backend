from flask import Blueprint, jsonify, request, make_response
from .. import db
from .models import Compound, Batch, Vial
from .schemas import CompoundSchema

# compound_api = Blueprint('compounds', __name__)
# compound_schema = CompoundSchema()
# compounds_schema = CompoundSchema(many=True)


# @compound_api.route('/compounds', methods=['GET', 'POST'])
# def compound_log_view():
#     compounds = Compound.query.all()

#     result = compounds_schema.dump(compounds)
#     return jsonify({'compounds': 123})

#hi