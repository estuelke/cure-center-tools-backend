import pytest
from datetime import datetime
from gql import Client
from gql.transport.requests import RequestsHTTPTransport
from config import Config
from backend.database.compound.models import Compound
from backend import db
from config import Config

settings = Config.MONGODB_SETTINGS
db_uri = f"mongodb://{settings['username']}:{settings['password']}@{settings['host']}" \
    f":{settings['port']}/{settings['db']}"


@pytest.fixture(scope='module')
def backend_db():
    db.connect(host=db_uri)
    reset_counters(db)
    Compound.drop_collection()

    yield db
    db.disconnect()


@pytest.fixture(scope='module')
def add_compounds():
    Compound(
        gsk_compound_num='1234',
        qtx_compound_num='QTX10001',
        date_created=datetime.utcnow(),
        date_updated=datetime.utcnow()
    ).save()

    Compound(
        gsk_compound_num='3456',
        qtx_compound_num='QTX10002',
        date_created=datetime.utcnow(),
        date_updated=datetime.utcnow()
    ).save()

    Compound(
        gsk_compound_num='5678',
        qtx_compound_num='QTX10003',
        date_created=datetime.utcnow(),
        date_updated=datetime.utcnow()
    ).save()


@pytest.fixture
def single_compound():
    compound4 = Compound(
        gsk_compound_num='9999',
        date_created=datetime.utcnow(),
        date_updated=datetime.utcnow()
    ).save()

    yield compound4

    compound4.delete()


@pytest.fixture
def compound_api():
    api_url = f"http://{Config.HOST}:{Config.FLASK_PORT}/graphql"
    headers = {'content-type': 'application/json'}

    transport = RequestsHTTPTransport(
        url=api_url,
        headers=headers,
        use_json=True,
        verify=False
    )

    client = Client(
        retries=3,
        transport=transport,
        fetch_schema_from_transport=True
    )

    return client


def reset_counters(client):
    db = client.get_db()
    counters = db.get_collection('mongoengine.counters')
    counters.update_one(
        {'_id': 'compound.qtx_compound_num'}, {"$set": {'next': 10003}}
    )
