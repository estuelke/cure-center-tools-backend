import pytest
import requests
from config import Config

api_url = f"http://{Config.HOST}:{Config.FLASK_PORT}/graphql"
headers = {'content-type': 'application/json'}


def test_compound_query():
    payload = '{"query": "{compound(id:\\"Q29tcG91bmQ6MTU=\\"){gskCompoundNum}}"}'
    response = requests.post(api_url, headers=headers, data=payload)
    json = response.json()

    assert response.status_code == 200
    assert json['data']['compound']['gskCompoundNum'] == 'GSK3684461A'


def test_all_compounds_query():
    payload = '{"query": "{allCompounds{edges{node{id}}}}"}'
    response = requests.post(api_url, headers=headers, data=payload)
    json = response.json()

    assert response.status_code == 200
    assert len(json['data']['allCompounds']['edges']) > 0
