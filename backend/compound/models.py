from backend import db


class Compound(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    compound_designation = db.Column(db.String(), unique=True, primary_key=True)

    # Identifying information
    bioduro_id = db.Column(db.String(20))
    bioduro_reference_code = db.Column(db.String(20))
    wuxi_reference_code = db.Column(db.String(20))
    qtx_compound_id = db.Column(db.String(10))

    # Chemical Structure properties
    molecular_weight = db.Column(db.Float)
    compound_class = db.Column(db.String(100))
    dimer_versus_monomer = db.Column(db.String(10))
    astx_versus_sbi_derivative = db.Column(db.String(5))
    dimerization_position = db.Column(db.String(30))
    p2_group = db.Column(db.String(20))
    p3_group = db.Column(db.String(20))
    pyridone_r = db.Column(db.String(20))

    # Other
    smiles_string = db.Column(db.Text)
    comments = db.Column(db.Text)

    # Legacy Columns
    gsk_log_number = db.Column(db.String(10))

    def __repr__(self):
        return f'<Compound(designation={self.compound_designation})>'


class Batch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lab_notebook_reference = db.Column(db.String())
    barcode = db.Column(db.String())
    chemist = db.Column(db.String())
    vendor = db.Column(db.String())
    vendor_catalog_number = db.Column(db.String())


class Vial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Identifying information
    date_entered = db.Column(db.String())
    qura_log_number = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String())
    owner_initials = db.Column(db.String())  # Relationship
    qura_project_code = db.Column(db.String())  # Relationship

    # Physical Properties
    concentration = db.Column(db.String())
    concentration_units = db.Column(db.String())
    weight = db.Column(db.String())
    weight_units = db.Column(db.String())
    vehicle = db.Column(db.String())
    vehicle_volume = db.Column(db.String())
    vehicle_volume_units = db.Column(db.String())

    # Other
    comments = db.Column(db.String())

    # Not critical but exists in original Excel log
    weighed_by = db.Column(db.String())
    location = db.Column(db.String())
    balance = db.Column(db.String())
    gsk_project_code = db.Column(db.String())
