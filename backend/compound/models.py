from backend import db
from datetime import datetime


class Compound(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)

    # Identifiers
    gsk_compound_num = db.Column(db.String(30), unique=True, nullable=True)
    qtx_compound_num = db.Column(db.String(20), unique=True, nullable=True)
    pubchem_compound_id = db.Column(db.String(30), unique=True, nullable=True)
    cas_num = db.Column(db.String(30), unique=True, nullable=True)

    # Properties for biologists
    drug_class = db.Column(db.String(120), nullable=True)
    analog_info = db.Column(db.String(120), nullable=True)
    screening_info = db.Column(db.String(120), nullable=True)

    # Properties for chemists
    molecular_weight = db.Column(db.Float, nullable=True)
    compound_class = db.Column(db.String(120), nullable=True)
    multimer_class = db.Column(db.String(30), nullable=True)
    dimerization_position = db.Column(db.String(30), nullable=True)
    p2_group = db.Column(db.String(20), nullable=True)
    p3_group = db.Column(db.String(20), nullable=True)
    p3_group_radical = db.Column(db.String(20), nullable=True)
    structure_reference_code = db.Column(db.String(30), nullable=True)
    smiles_string = db.Column(db.Text, nullable=True)

    # Other
    comments = db.Column(db.Text, nullable=True)
    date_added = db.Column(db.DateTime, nullable=True)

    # Relationships
    batches = db.relationship('Batch', backref='Compound', lazy=True)
    vials = db.relationship('Vial', backref='Compound', lazy=True)

    def get_compound_represenation(self):
        d = {
            'GSK Compound #': self.gsk_compound_num,
            'QTX Compound #': self.qtx_compound_num,
            'CAS #': self.cas_num,
            'PubChem ID': self.pubchem_compound_id
        }

        return [(k, v) for (k, v) in d.items() if v is not None]

    def __repr__(self):
        return f'<Compound({self.get_compound_represenation()})>'


class Batch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    compound_id = db.Column(
        db.Integer, db.ForeignKey('compound.id'), nullable=False
    )

    # Batch Identifiers
    lnb_reference = db.Column(db.String(30), nullable=True)
    source_reference = db.Column(db.String(50), nullable=True)
    source_barcode = db.Column(db.String(50), nullable=True)
    lot_num = db.Column(db.String(50), nullable=True)

    # Source Information
    source_name = db.Column(db.String(120), nullable=True)

    # Synthesis Information
    chemist = db.Column(db.String(50), nullable=True)
    date_synthesized = db.Column(db.DateTime, nullable=True)

    # External Synthesis Information
    shipment_num = db.Column(db.String(20), nullable=True)

    # Order Information
    date_ordered = db.Column(db.DateTime, nullable=True)
    ordered_by = db.Column(db.String(50), nullable=True)
    catalog_number = db.Column(db.String(100), nullable=True)
    date_received = db.Column(db.DateTime, nullable=True)

    # Relationships
    vials = db.relationship('Vial', backref='batch', lazy=True)

    def get_batch_represenation(self):
        d = {
            'LNB Reference': self.lnb_reference,
            'Source Reference': self.source_reference,
            'Lot #': self.lot_num,
            'Source': self.source_name,
            'Catalog #': self.catalog_number
        }

        return [(k, v) for (k, v) in d.items() if v is not None]

    def __repr__(self):
        return f'<Compound({self.get_batch_represenation()})>'


class Vial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qura_log_num = db.Column(
        db.Integer, autoincrement=True, nullable=False
    )
    compound_id = db.Column(
        db.Integer, db.ForeignKey('compound.id'), nullable=False
    )
    batch_id = db.Column(db.Integer, db.ForeignKey('batch.id'), nullable=False)

    # Vial Properties
    date_entered = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    barcode = db.Column(db.String(50), nullable=True)
    owner_initials = db.Column(db.String(10), nullable=False)
    weighed_by = db.Column(db.String(50), nullable=True)
    qura_project_code = db.Column(db.String(30), nullable=True)
    gsk_project_code = db.Column(db.String(20), nullable=True)
    is_empty = db.Column(db.Boolean)

    # Material Properties
    concentration = db.Column(db.Float, nullable=True)
    concentration_units = db.relationship('Unit', lazy=True)
    weight = db.Column(db.Float, nullable=True)
    weight_units = db.relationship('Unit', lazy=True)
    vehicle = db.Column(db.String(50), nullable=True, default='DMSO')
    vehicle_volume = db.Column(db.Float, nullable=True)
    vehicle_volume_units = db.relationship('Unit', lazy=True)
    is_solid = db.Column(db.Boolean)

    # Other
    comment = db.Column(db.Text, nullable=True)

    # Relationships
    parent_vial_id = db.Column(db.Integer, db.ForeignKey('vial.id'))
    parent_vial = db.relationship(
        'Vial',
        backref='vial_parent_vial',
        uselist=False,
        remote_side=[id],
        lazy=True
    )

    # Not critical but exists in original Excel log
    location = db.Column(db.String(50), nullable=True)
    balance = db.Column(db.String(50), nullable=True)
    gsk_log_num = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f'<Vial({self.qura_log_num})>'


class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unit = db.Column(db.String(20), nullable=False)
    classification = db.Column(db.String(20), nullable=False)
    multiplier = db.Column(db.Integer, nullable=False)
