"""empty message

Revision ID: aa5470014f0a
Revises: 17430108f6de
Create Date: 2019-12-21 16:16:06.390047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa5470014f0a'
down_revision = '17430108f6de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient', sa.Column('email', sa.CHAR(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patient', 'email')
    # ### end Alembic commands ###
