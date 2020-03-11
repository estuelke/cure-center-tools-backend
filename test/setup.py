import pytest
from backend.compound.models import Compound
from backend import db
from config import Config

settings = Config.MONGODB_SETTINGS
db_uri = f"mongodb://{settings['username']}:{settings['password']}@{settings['host']}" \
    ":{settings['port']}/{settings['db']}"


@pytest.fixture(scope='module')
def fixtures():
    db.connect(host=db_uri)

    Compound.drop_collection()
    compound1 = Compound(
        gsk_compound_num='1234'
    )
    compound1.save()

    compound2 = Compound(
        gsk_compound_num='3456'
    )
    compound2.save()

    compound3 = Compound(
        gsk_compound_num='5678'
    )
    compound3.save()

    yield db
    db.disconnect()
