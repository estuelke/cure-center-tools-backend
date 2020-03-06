import pandas as pd
from alembic import op
import sqlalchemy as sa
from config import Config

member_file = Config.MEMBER_SEED_FILE
compound_file = Config.COMPOUND_SEED_FILE

member_columns = {
    'list_memberships': [
        sa.sql.column('list_id', sa.Integer),
        sa.sql.column('member_id', sa.Integer)
    ],
    'member': [
        sa.sql.column('id', sa.Integer),
        sa.sql.column('first_name', sa.String),
        sa.sql.column('last_name', sa.String),
        sa.sql.column('institution', sa.String),
        sa.sql.column('is_executive_assistant', sa.Boolean),
        sa.sql.column('executive_assistant_id', sa.String)
    ],
    'cure_center_profile': [
        sa.sql.column('id', sa.Integer),
        sa.sql.column('member_id', sa.Integer),
        sa.sql.column('nick_name', sa.String),
        sa.sql.column('suffix', sa.String),
        sa.sql.column('birthday', sa.Date),
        sa.sql.column('group_id', sa.Integer),
        sa.sql.column('is_internal', sa.Boolean),
        sa.sql.column('is_qura_funded', sa.Boolean),
        sa.sql.column('image_url', sa.String),
        sa.sql.column('staff_designation', sa.String)
    ],
    'email': [
        sa.sql.column('member_id', sa.Integer),
        sa.sql.column('label', sa.String),
        sa.sql.column('email_address', sa.String)
    ],
    'group': [
        sa.sql.column('id', sa.Integer),
        sa.sql.column('contact_id', sa.Integer),
        sa.sql.column('name', sa.String),
    ],
    'list': [
        sa.sql.column('id', sa.Integer),
        sa.sql.column('name', sa.String),
        sa.sql.column('list_type', sa.String),
        sa.sql.column('description', sa.String)
    ],
    'phone_number': [
        sa.sql.column('member_id', sa.Integer),
        sa.sql.column('label', sa.String),
        sa.sql.column('phone_number', sa.String)
    ],
    'position': [
        sa.sql.column('cure_center_profile_id', sa.Integer),
        sa.sql.column('title', sa.String),
        sa.sql.column('department', sa.String)
    ]
}


def member_seed_data():
    tables = pd.read_excel(member_file, sheet_name=None)
    for name, table in tables.items():
        if name == 'cure_center_profile':
            table.drop(columns=['birthday'], inplace=True)
        try:
            db_table = sa.sql.table(name, *member_columns[name])
            table.fillna('', inplace=True)
            data = table.to_dict('records')
            op.bulk_insert(
                db_table,
                data
            )
        except Exception as e:
            print(f"Error found {e}: Sheet: {name}")


compound_columns = {
    "compound": [
        sa.sql.column('id', sa.Integer),
        sa.sql.column('gsk_compound_num', sa.String)
    ]
}


def compound_seed_data():
    compounds = pd.read_excel(compound_file)
    compounds = compounds.filter(['GSK Compound #'])
    compounds = compounds.drop_duplicates()
    compounds = compounds.rename(columns={'GSK Compound #': 'gsk_compound_num'})

    db_table = sa.sql.table('compound', *compound_columns['compound'])
    data = compounds.to_dict('records')
    print(data)
    op.bulk_insert(
        db_table,
        data
    )
