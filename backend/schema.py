import graphene
from .database.compound.schema import Mutation as CompoundMutation, Query as CompoundQuery
from .database.compound.schema import Compound


class Query(CompoundQuery, graphene.ObjectType):
    pass


class Mutation(CompoundMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, types=[Compound])
