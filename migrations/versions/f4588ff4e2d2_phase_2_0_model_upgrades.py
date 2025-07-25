"""Phase 2.0 Model Upgrades

Revision ID: f4588ff4e2d2
Revises: 6cced95292b1
Create Date: 2025-04-28 12:15:34.544684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4588ff4e2d2'
down_revision = '6cced95292b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_active', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('badges', sa.String(length=512), nullable=True))
        batch_op.add_column(sa.Column('streak_days', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('streak_days')
        batch_op.drop_column('badges')
        batch_op.drop_column('last_active')

    # ### end Alembic commands ###
