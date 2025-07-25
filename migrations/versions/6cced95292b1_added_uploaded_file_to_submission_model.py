"""Added uploaded_file to Submission model

Revision ID: 6cced95292b1
Revises: 4cc20a8206e8
Create Date: 2025-04-24 01:45:50.811517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cced95292b1'
down_revision = '4cc20a8206e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('submission', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uploaded_file', sa.String(length=256), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('submission', schema=None) as batch_op:
        batch_op.drop_column('uploaded_file')

    # ### end Alembic commands ###
