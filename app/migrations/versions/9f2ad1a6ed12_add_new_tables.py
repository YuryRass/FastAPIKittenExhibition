"""Add new tables

Revision ID: 9f2ad1a6ed12
Revises: 8876ed7fded2
Create Date: 2024-10-01 22:23:49.095590

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f2ad1a6ed12'
down_revision: Union[str, None] = '8876ed7fded2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('breeds',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_breeds_name'), 'breeds', ['name'], unique=True)
    op.create_table('kittens',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('color', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('breed_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['breed_id'], ['breeds.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_kittens_name'), 'kittens', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_kittens_name'), table_name='kittens')
    op.drop_table('kittens')
    op.drop_index(op.f('ix_breeds_name'), table_name='breeds')
    op.drop_table('breeds')
    # ### end Alembic commands ###
