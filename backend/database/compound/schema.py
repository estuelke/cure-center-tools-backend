import graphene
from datetime import datetime
from graphene import InputObjectType, relay
from graphene_mongo import MongoengineObjectType, MongoengineConnectionField
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


class UpdateCompoundInput(InputObjectType, CompoundAttribute):
    pass


class UpdateCompound(graphene.Mutation):
    compound = graphene.Field(lambda: Compound, description='Compound updated by this mutation.')

    class Arguments:
        id = graphene.String(required=True, description="Id of the compound.")
        input = UpdateCompoundInput(required=True)

    def mutate(self, info, id, input):
        input['date_updated'] = datetime.utcnow()
        # id = relay.Node.from_global_id(global_id)[1]

        CompoundModel.objects(id=id).first().update(**input)
        compound = CompoundModel.objects(id=id).first()

        return UpdateCompound(compound=compound)


class Mutation(graphene.ObjectType):
    create_compound = CreateCompound.Field()
    update_compound = UpdateCompound.Field()


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    compound = graphene.Field(Compound)
    compounds = MongoengineConnectionField(Compound)

    def resolve_compound(self, info):
        return CompoundModel.objects.first()

    def resolve_compounds(self, info):
        return CompoundModel.objects.all()
