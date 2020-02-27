from flask import Blueprint, jsonify, request
# from backend import db
import pandas as pd
# include forms, models here

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def index():
    df = pd.DataFrame([['a', 'b'], ['c', 'd']],
                      index=['row 1', 'row 2'],
                      columns=['col 1', 'col 2'])
    print('In index route of main')
    return df.to_json(orient='split')
