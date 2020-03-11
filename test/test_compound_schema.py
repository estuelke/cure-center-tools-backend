import pytest
from .setup import fixtures
from backend.schema import schema


def test_should_query_compound(fixtures):
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

    result = schema.execute(query)

    assert not result.errors
    assert result.data == expected


def test_should_return_all_compounds(fixtures):
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

    result = schema.execute(query)

    assert not result.errors
    assert result.data == expected
