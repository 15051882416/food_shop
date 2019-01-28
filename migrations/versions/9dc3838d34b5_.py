"""empty message

Revision ID: 9dc3838d34b5
Revises: a61178aafb4c
Create Date: 2019-01-24 16:33:16.115592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dc3838d34b5'
down_revision = 'a61178aafb4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('name', sa.String(length=30), nullable=True, comment='name'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('image', 'name')
    # ### end Alembic commands ###
