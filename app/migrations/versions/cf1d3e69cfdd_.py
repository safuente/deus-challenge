"""

Revision ID: cf1d3e69cfdd
Revises: 
Create Date: 2025-03-06 09:00:47.110062

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf1d3e69cfdd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('contact_info', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('client_id')
    )
    op.create_index(op.f('ix_clients_client_id'), 'clients', ['client_id'], unique=False)
    op.create_index(op.f('ix_clients_name'), 'clients', ['name'], unique=False)
    op.create_table('vessels',
    sa.Column('vessel_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('capacity', sa.Float(), nullable=True),
    sa.Column('current_location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('vessel_id')
    )
    op.create_index(op.f('ix_vessels_name'), 'vessels', ['name'], unique=False)
    op.create_index(op.f('ix_vessels_vessel_id'), 'vessels', ['vessel_id'], unique=False)
    op.create_table('contracts',
    sa.Column('contract_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('destination', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['clients.client_id'], ),
    sa.PrimaryKeyConstraint('contract_id')
    )
    op.create_index(op.f('ix_contracts_contract_id'), 'contracts', ['contract_id'], unique=False)
    op.create_table('cargoes',
    sa.Column('cargo_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('volume', sa.Float(), nullable=True),
    sa.Column('contract_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['contract_id'], ['contracts.contract_id'], ),
    sa.PrimaryKeyConstraint('cargo_id')
    )
    op.create_index(op.f('ix_cargoes_cargo_id'), 'cargoes', ['cargo_id'], unique=False)
    op.create_table('tracking',
    sa.Column('tracking_id', sa.Integer(), nullable=False),
    sa.Column('cargo_id', sa.Integer(), nullable=True),
    sa.Column('vessel_id', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['cargo_id'], ['cargoes.cargo_id'], ),
    sa.ForeignKeyConstraint(['vessel_id'], ['vessels.vessel_id'], ),
    sa.PrimaryKeyConstraint('tracking_id')
    )
    op.create_index(op.f('ix_tracking_tracking_id'), 'tracking', ['tracking_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tracking_tracking_id'), table_name='tracking')
    op.drop_table('tracking')
    op.drop_index(op.f('ix_cargoes_cargo_id'), table_name='cargoes')
    op.drop_table('cargoes')
    op.drop_index(op.f('ix_contracts_contract_id'), table_name='contracts')
    op.drop_table('contracts')
    op.drop_index(op.f('ix_vessels_vessel_id'), table_name='vessels')
    op.drop_index(op.f('ix_vessels_name'), table_name='vessels')
    op.drop_table('vessels')
    op.drop_index(op.f('ix_clients_name'), table_name='clients')
    op.drop_index(op.f('ix_clients_client_id'), table_name='clients')
    op.drop_table('clients')
    # ### end Alembic commands ###
