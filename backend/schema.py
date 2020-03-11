import graphene
from .compound.schema import Mutation as CompoundMutation, Query as CompoundQuery
from .compound.schema import Compound


class Query(CompoundQuery, graphene.ObjectType):
    pass


class Mutation(CompoundMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, types=[Compound])
