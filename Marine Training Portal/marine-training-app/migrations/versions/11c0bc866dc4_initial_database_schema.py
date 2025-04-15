"""Initial database schema

Revision ID: 11c0bc866dc4
Revises: 
Create Date: 2025-04-01 22:13:43.620923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11c0bc866dc4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'course_enrollment',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('course.id'), nullable=False)
    )

    # ### end Alembic commands ###


def downgrade():
    op.drop_table('course_enrollment')

    # ### end Alembic commands ###
