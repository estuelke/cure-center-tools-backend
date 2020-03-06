import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from .compound.schema import Compound


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    compound = relay.Node.Field(Compound)
    all_compounds = SQLAlchemyConnectionField(Compound)


schema = graphene.Schema(query=Query)
