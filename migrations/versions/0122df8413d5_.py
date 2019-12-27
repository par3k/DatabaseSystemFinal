"""empty message

Revision ID: 0122df8413d5
Revises: fd01de9f946d
Create Date: 2019-12-21 17:06:06.193621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0122df8413d5'
down_revision = 'fd01de9f946d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('department_ibfk_1', 'department', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('department_ibfk_1', 'department', 'medicalstaff', ['doctor_ID'], ['StaffID'])
    # ### end Alembic commands ###