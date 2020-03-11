import graphene
from datetime import datetime
from graphene import InputObjectType, relay
from graphene_mongo import MongoengineObjectType
from .models import Compound as CompoundModel


class CompoundAttribute:
    gsk_compound_num = graphene.String(description='GSK compound registration number.')
    qtx_compound_num = graphene.String(description='Qura compound registration number.')
    pubchem_compound_id = graphene.List(graphene.String, description='Compound IDs from PubChem database.')
    cas_num = graphene.String(description='CAS Registry number.')

    drug_class = graphene.List(graphene.String, description='Drug/Compound target or class.')
    molecular_weight = graphene.Float(description='Molecular weight of compound.')
    structure_reference_code = graphene.String(description='UNC internal chemist code.')
    smiles_string = graphene.String(description='String representation of compound structure.')

    date_created = graphene.DateTime(description='Date compound added to log.')
    date_updated = graphene.DateTime(description='Date compound last edited.')


class Compound(MongoengineObjectType, CompoundAttribute):
    class Meta:
        model = CompoundModel
        interfaces = (relay.Node, )


class CreateCompoundInput(InputObjectType, CompoundAttribute):
    pass


class CreateCompound(graphene.Mutation):
    compound = graphene.Field(lambda: Compound, description='Compound created by this mutation')

    class Arguments:
        input = CreateCompoundInput(required=True)

    def mutate(self, info, input):
        input['date_created'] = datetime.utcnow()
        input['date_updated'] = datetime.utcnow()

        compound = CompoundModel(**input).save()

        return CreateCompound(compound=compound)


class UpdateCompound():
    pass


class Mutation(graphene.ObjectType):
    create_compound = CreateCompound.Field()


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    compound = graphene.Field(Compound)
    compounds = graphene.List(Compound)

    def resolve_compound(self, *args, **kwargs):
        return CompoundModel.objects.first()

    def resolve_compounds(self, info):
        return CompoundModel.objects.all()
