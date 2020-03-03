import pandas as pd
from alembic import op
import sqlalchemy as sa
from config import Config

filename = Config.COMPOUND_SEED_FILE

columns = {
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
    ]
}


def seed_data():
    data = pd.read_excel(filename, sheet_name=None)

    # try:
    #     db_table = sa.sql.table('compound', *columns['compound'])
    #     data.fillna('', inplace=True)
    #     data = data.to_dict('records')
    #     op.bulk_insert(
    #         db_table,
    #         data
    #     )
    # except Exception as e:
    #     print(f"Error found {e}: Sheet: {name}")
