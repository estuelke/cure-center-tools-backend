import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from .models import Compound as CompoundModel


class CompoundAttribute:
    gsk_compound_num = graphene.String(
        description="GSK compound registration number."
    )


class Compound(SQLAlchemyObjectType, CompoundAttribute):
    class Meta:
        model = CompoundModel
        interfaces = (relay.Node, )
