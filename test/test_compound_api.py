import pytest  # noqa: F401
from gql import gql
from graphene.relay.node import to_global_id
from .setup import backend_db, add_compounds, compound_api, single_compound  # noqa F401
from .queries import GET_COMPOUND_BY_ID_USING_NODE, GET_ALL_COMPOUNDS, GET_FIRST_COMPOUND


class TestCompoundQueryAPI:
    def test_should_get_compound_by_id_through_node(self, backend_db, single_compound, compound_api):  # noqa F811
        query = gql(GET_COMPOUND_BY_ID_USING_NODE)
        global_id = to_global_id('Compound', single_compound.id)

        params = {
            "id": global_id
        }

        expected = {
            'node': {
                'id': global_id,
                'gskCompoundNum': '9999'
            }
        }

        result = compound_api.execute(query, variable_values=params)
        assert result == expected

    def test_should_get_first_compound(self, backend_db, add_compounds, compound_api):  # noqa F811
        query = gql(GET_FIRST_COMPOUND)

        expected = {
            'compound': {
                'gskCompoundNum': '1234'
            }
        }

        result = compound_api.execute(query)
        assert result == expected

    def test_should_return_all_compounds_api(self, backend_db, add_compounds, compound_api):  # noqa F811
        query = gql(GET_ALL_COMPOUNDS)

        expected = {
            'compounds': {
                'edges': [
                    {"node": {'gskCompoundNum': '1234'}},
                    {"node": {'gskCompoundNum': '3456'}},
                    {"node": {'gskCompoundNum': '5678'}}
                ]
            }
        }

        result = compound_api.execute(query)
        assert result == expected
