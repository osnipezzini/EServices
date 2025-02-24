# encoding: utf-8
"""Initial struct

Revision ID: fbae82ca9b57
Revises: 
Create Date: 2020-02-17 20:56:37.930329

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import Sequence
from sqlalchemy.sql.ddl import CreateSequence

from core import log

revision = 'fbae82ca9b57'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    log.debug('Creating tables ...')
    op.execute(CreateSequence(Sequence('grid_seq')))
    person_group = op.create_table('person_group',
                                   sa.Column('grid', sa.BigInteger(), sa.Sequence('grid_seq'), nullable=False),
                                   sa.Column('code', sa.Integer(), sa.Sequence('person_group_code_seq'), nullable=True),
                                   sa.Column('name', sa.String(length=250), nullable=False),
                                   sa.Column('flag', sa.CHAR(length=1), nullable=False, default='A'),
                                   sa.PrimaryKeyConstraint('grid')
                                   )
    op.execute(CreateSequence(Sequence('person_group_code_seq')))
    person = op.create_table('person',
                             sa.Column('grid', sa.BigInteger(), sa.Sequence('grid_seq'), nullable=False),
                             sa.Column('code', sa.Integer(), sa.Sequence('person_code_seq'), nullable=True, ),
                             sa.Column('doc', sa.String(length=20), nullable=False),
                             sa.Column('name', sa.String(length=250), nullable=False),
                             sa.Column('email', sa.String(length=200), nullable=False),
                             sa.Column('flag', sa.CHAR(length=1), nullable=False, default='A'),
                             sa.Column('city_code', sa.String(length=10), nullable=False),
                             sa.Column('city_name', sa.String(length=100), nullable=False),
                             sa.Column('state', sa.String(length=50), nullable=False),
                             sa.Column('zipcode', sa.String(length=10), nullable=True),
                             sa.Column('district', sa.String(length=50), nullable=True),
                             sa.Column('country', sa.String(length=50), nullable=True),
                             sa.Column('address', sa.Unicode(length=50), nullable=True),
                             sa.Column('address_nr', sa.String(length=50), nullable=False),
                             sa.Column('group_grid', sa.Integer(), nullable=True),
                             sa.ForeignKeyConstraint(['group_grid'], ['person_group.grid'], ),
                             sa.PrimaryKeyConstraint('grid')
                             )
    op.execute(CreateSequence(Sequence('person_code_seq')))
    product = op.create_table('product',
                              sa.Column('grid', sa.BigInteger(), sa.Sequence('grid_seq'), nullable=False),
                              sa.Column('code', sa.Integer(), sa.Sequence('product_code_seq'), nullable=True),
                              sa.Column('barcode', sa.String(length=50), nullable=False),
                              sa.Column('name', sa.String(length=250), nullable=False),
                              sa.Column('price', sa.Float(), nullable=False),
                              sa.Column('person_id', sa.Integer(), nullable=True),
                              sa.ForeignKeyConstraint(['person_id'], ['person.grid'], ),
                              sa.PrimaryKeyConstraint('grid'),
                              sa.UniqueConstraint('code')
                              )
    op.execute(CreateSequence(Sequence('product_code_seq')))
    # ### end Alembic commands ###
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)
    person_group_data = list()
    person_group_data.append({'name': 'EMPRESA'})
    person_group_data.append({'name': 'CLIENTES'})
    person_group_data.append({'name': 'FORNECEDORES'})
    person_group_data.append({'name': 'FUNCIONARIOS'})
    log.debug('Populate person_group table')
    for pg in person_group_data:
        session.execute(sa.insert(person_group).values(pg))
    log.debug('Populate person table')
    person_data = {
        'name': 'EMPRESA REGISTRADA', 'email': 'teste@teste.com', 'doc': '00.000.000/0000-00',
        'city_code': '4202404', 'city_name': 'Blumenau', 'state': 'SC', 'zipcode': '89010-000',
        'district': "Centro", 'country': 'Brasil', 'address': 'Rua XV de Novembro', 'address_nr': '45',
        'group_grid': 1
    }
    session.execute(sa.insert(person).values(person_data))


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('person')
    op.drop_table('person_group')
    # ### end Alembic commands ###
