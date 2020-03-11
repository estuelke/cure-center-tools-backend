import pytest
import requests
from config import Config
from .setup import fixtures
from backend.schema import schema

api_url = f"http://{Config.HOST}:{Config.FLASK_PORT}/graphql"
headers = {'content-type': 'application/graphql'}


def test_should_query_compound_api(fixtures):
    query = """
        query CompoundQuery {
            compound {
                gskCompoundNum
            }
        }
    """.strip()

    expected = {
        'compound': {
            'gskCompoundNum': '1234'
        }
    }

    response = requests.post(api_url, headers=headers, data=query)
    result = response.json()

    assert response.status_code == 200
    assert result['data'] == expected


def test_should_return_all_compounds_api(fixtures):
    query = """
        query CompoundsQuery {
            compounds {
                gskCompoundNum
            }
        }
    """.strip()

    expected = {
        'compounds': [{
            'gskCompoundNum': '1234'
        }, {
            'gskCompoundNum': '3456'
        }, {
            'gskCompoundNum': '5678'
        }]
    }
    response = requests.post(api_url, headers=headers, data=query)
    result = response.json()

    assert response.status_code == 200
    assert result['data'] == expected
