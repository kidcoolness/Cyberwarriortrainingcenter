"""Add platoon hierarchy and foreign keys

Revision ID: 3e12e9408afa
Revises: 2ade8fdb1088
Create Date: 2025-06-03 04:31:12.349257

"""
from alembic import op
import sqlalchemy as sa

revision = '3e12e9408afa'
down_revision = '2ade8fdb1088'
branch_labels = None
depends_on = None

def upgrade():
    # Create new unit tables
    op.create_table(
        'platoon',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False, unique=True)
    )

    op.create_table(
        'mission_element',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('platoon_id', sa.Integer(), sa.ForeignKey('platoon.id'), nullable=False)
    )

    op.create_table(
        'team',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('mission_element_id', sa.Integer(), sa.ForeignKey('mission_element.id'), nullable=False)
    )

    # Add new foreign key fields to User model — keep old columns for now
    op.add_column('user', sa.Column('platoon_id', sa.Integer(), sa.ForeignKey('platoon.id'), nullable=True))
    op.add_column('user', sa.Column('mission_element_id', sa.Integer(), sa.ForeignKey('mission_element.id'), nullable=True))
    op.add_column('user', sa.Column('team_id', sa.Integer(), sa.ForeignKey('team.id'), nullable=True))
