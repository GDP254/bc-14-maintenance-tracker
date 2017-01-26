"""empty message

Revision ID: 669520b92ead
Revises: 451e884b232b
Create Date: 2017-01-26 16:07:01.191000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '669520b92ead'
down_revision = '451e884b232b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'request_admin_id_fkey', 'request', type_='foreignkey')
    op.drop_constraint(u'request_facility_id_fkey', 'request', type_='foreignkey')
    op.drop_constraint(u'request_user_id_fkey', 'request', type_='foreignkey')
    op.drop_column('request', 'user_id')
    op.drop_column('request', 'admin_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('request', sa.Column('admin_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('request', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'request_user_id_fkey', 'request', 'users', ['user_id'], ['id'])
    op.create_foreign_key(u'request_facility_id_fkey', 'request', 'facilities', ['facility_id'], ['id'])
    op.create_foreign_key(u'request_admin_id_fkey', 'request', 'users', ['admin_id'], ['id'])
    # ### end Alembic commands ###
