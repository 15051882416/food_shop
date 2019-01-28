"""empty message

Revision ID: b6d9fb24ca94
Revises: d1c36eb15446
Create Date: 2019-01-25 21:21:31.039547

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b6d9fb24ca94'
down_revision = 'd1c36eb15446'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_callback_data')
    op.alter_column('access_token', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('app_access_log', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('app_error_log', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('food', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('food_cat', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('food_sale_change_log', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('food_stock_change_log', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('image', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('member', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('member_address', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('member_cart', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('member_client', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('member_comment', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('order', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('order_food', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.add_column('queue', sa.Column('handle_status', sa.SmallInteger(), nullable=True, comment='处理的状态: 0, 未处理(默认) 1, 已处理'))
    op.alter_column('queue', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('stat_daily_food', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('stat_daily_member', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('stat_daily_site', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('user', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('wx_share_history', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='状态: 1, 存在; 0, 删除;',
               existing_comment='用户状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('wx_share_history', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('user', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('stat_daily_site', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('stat_daily_member', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('stat_daily_food', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('queue', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.drop_column('queue', 'handle_status')
    op.alter_column('order_food', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('order', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('member_comment', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('member_client', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('member_cart', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('member_address', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('member', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('image', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('food_stock_change_log', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('food_sale_change_log', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('food_cat', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('food', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('app_error_log', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('app_access_log', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.alter_column('access_token', 'status',
               existing_type=mysql.SMALLINT(display_width=6),
               comment='用户状态: 1, 存在; 0, 删除;',
               existing_comment='状态: 1, 存在; 0, 删除;',
               existing_nullable=False)
    op.create_table('order_callback_data',
    sa.Column('create_time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False, comment='创建时间'),
    sa.Column('update_time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False, comment='更新时间'),
    sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False, comment='用户状态: 1, 存在; 0, 删除;'),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('order_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False, comment='支付订单id'),
    sa.Column('pay_data', mysql.TEXT(), nullable=False, comment='支付回调信息'),
    sa.Column('refund_data', mysql.TEXT(), nullable=False, comment='退款回调信息'),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], name='order_callback_data_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###