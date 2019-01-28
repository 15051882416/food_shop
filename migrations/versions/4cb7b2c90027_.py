"""empty message

Revision ID: 4cb7b2c90027
Revises: e00af350376d
Create Date: 2019-01-26 21:01:16.965421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cb7b2c90027'
down_revision = 'e00af350376d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stat_daily_food', sa.Column('date', sa.String(length=10), nullable=False, comment='统计日期'))
    op.add_column('stat_daily_member', sa.Column('date', sa.String(length=10), nullable=False, comment='统计日期'))
    op.add_column('stat_daily_site', sa.Column('date', sa.String(length=10), nullable=False, comment='统计日期'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stat_daily_site', 'date')
    op.drop_column('stat_daily_member', 'date')
    op.drop_column('stat_daily_food', 'date')
    # ### end Alembic commands ###
