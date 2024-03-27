"""empty message

Revision ID: 0e1ebe1efe38
Revises: 
Create Date: 2024-03-27 10:50:38.024586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e1ebe1efe38'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apparatuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('moves',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('apparatus_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['apparatus_id'], ['apparatuses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('routines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('apparatus_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['apparatus_id'], ['apparatuses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('routine_moves',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('routine_id', sa.Integer(), nullable=True),
    sa.Column('move_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['move_id'], ['moves.id'], ),
    sa.ForeignKeyConstraint(['routine_id'], ['routines.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('routine_moves')
    op.drop_table('routines')
    op.drop_table('moves')
    op.drop_table('users')
    op.drop_table('apparatuses')
    # ### end Alembic commands ###