"""add pet owner assoc table

Revision ID: 330dd11e71f8
Revises: c3591ceaa0f5
Create Date: 2023-11-14 06:48:32.062805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '330dd11e71f8'
down_revision = 'c3591ceaa0f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_owners')),
    sa.UniqueConstraint('email', name=op.f('uq_owners_email')),
    sa.UniqueConstraint('phone', name=op.f('uq_owners_phone'))
    )
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('species', sa.String(), nullable=True),
    sa.Column('breed', sa.String(), nullable=True),
    sa.Column('temperament', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.CheckConstraint('length(name) > 0', name=op.f('ck_pets_`owner_name_length`')),
    sa.ForeignKeyConstraint(['owner_id'], ['owners.id'], name=op.f('fk_pets_owner_id_owners')),
    sa.PrimaryKeyConstraint('id', name='owner_pk')
    )
    op.create_table('pet_owner',
    sa.Column('pet_id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['owners.id'], name=op.f('fk_pet_owner_owner_id_owners')),
    sa.ForeignKeyConstraint(['pet_id'], ['pets.id'], name=op.f('fk_pet_owner_pet_id_pets')),
    sa.PrimaryKeyConstraint('pet_id', 'owner_id', name=op.f('pk_pet_owner'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pet_owner')
    op.drop_table('pets')
    op.drop_table('owners')
    # ### end Alembic commands ###