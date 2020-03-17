import pytest  # noqa: F401
from .setup import backend_db, add_compounds, single_compound # noqa F401
from backend.schema import schema
from .queries import GET_ALL_COMPOUNDS, GET_FIRST_COMPOUND, GET_COMPOUND_BY_ID_USING_NODE
from .mutations import CREATE_COMPOUND, UPDATE_COMPOUND
from graphene.relay.node import to_global_id


class TestCompoundQueries:
    def test_should_query_first_compound(self, backend_db, add_compounds):  # noqa F811
        expected = {
            'compound': {
                'gskCompoundNum': '1234'
            }
        }

        result = schema.execute(GET_FIRST_COMPOUND)

        assert not result.errors
        assert result.data == expected

    def test_should_query_compound_by_id_through_node(self, backend_db, single_compound):  # noqa F811
        global_id = to_global_id('Compound', single_compound.id)
        expected = {
            "node": {
                "id": global_id,
                "gskCompoundNum": "9999"
            }
        }
        result = schema.execute(GET_COMPOUND_BY_ID_USING_NODE, variable_values={'id': global_id})

        assert not result.errors
        assert result.data == expected

    def test_should_return_all_compounds(self, backend_db, add_compounds):  # noqa F811
        expected = {
            'compounds': {
                'edges': [
                    {"node": {'gskCompoundNum': '1234'}},
                    {"node": {'gskCompoundNum': '3456'}},
                    {"node": {'gskCompoundNum': '5678'}}
                ]
            }
        }

        result = schema.execute(GET_ALL_COMPOUNDS)

        assert not result.errors
        assert result.data == expected


class TestCompoundMutations:

    def test_should_create_compound(self, backend_db):  # noqa F811
        expected = {
            'createCompound': {'compound': {'gskCompoundNum': '123456'}}
        }
        result = schema.execute(CREATE_COMPOUND)

        assert not result.errors
        assert result.data == expected

    def test_should_update_compound(self, backend_db, single_compound):  # noqa F811
        global_id = to_global_id('Compound', single_compound.id)

        expected = {
            'updateCompound': {
                'compound': {
                    'gskCompoundNum': '8888',
                    'id': global_id
                }
            }
        }

        result = schema.execute(
            UPDATE_COMPOUND,
            variables={
                'id': single_compound.id,
                'input': {'gskCompoundNum': '8888'}
            }
        )

        assert not result.errors
        assert result.data == expected
        assert '8888' != single_compound.gsk_compound_num
