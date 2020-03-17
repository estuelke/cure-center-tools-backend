from backend import db
# from backend.database.batch.models import Batch
# from backend.database.vial.models import Vial


class Compound(db.DynamicDocument):
    meta = {'collection': 'compound'}

    # Relationships
    # batches = db.ListField(db.ReferenceField(Batch))
    # vials = db.ListField(db.ReferenceField(Vial))

    # Identifiers
    gsk_compound_num = db.StringField(max_length=30, unique=True, sparse=True, required=False)
    qtx_compound_num = db.SequenceField(
        value_decorator='QTX{}'.format, unique=True
    )
    pubchem_compound_id = db.ListField()
    cas_num = db.StringField(max_length=30, unique=True, sparse=True, required=False)

    # Properties
    drug_class = db.ListField()
    molecular_weight = db.FloatField(precision=3)
    structure_reference_code = db.StringField(max_length=30)
    smiles_string = db.StringField()

    # Other
    tags = db.ListField()
    date_created = db.DateTimeField()
    date_updated = db.DateTimeField()
