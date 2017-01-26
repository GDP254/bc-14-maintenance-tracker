"""empty message

Revision ID: 451e884b232b
Revises: d4c9cd9cc7a1
Create Date: 2017-01-26 07:01:04.777000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '451e884b232b'
down_revision = 'd4c9cd9cc7a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('photo', sa.String(length=64), nullable=True),
    sa.Column('notes', sa.String(length=200), nullable=True),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('facility_id', sa.Integer(), nullable=True),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.Column('admin_comment', sa.String(length=200), nullable=True),
    sa.Column('assignee_name', sa.String(length=64), nullable=True),
    sa.Column('assignee_number', sa.String(length=64), nullable=True),
    sa.Column('assignment_date', sa.String(length=64), nullable=True),
    sa.Column('assignment_time', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['facility_id'], ['facilities.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('request')
    # ### end Alembic commands ###