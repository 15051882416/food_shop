from sqlalchemy import Column, Integer, ForeignKey

from . import Base


class MemberCart(Base):
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('member.id'), nullable=False, comment='会员ID')
    food_id = Column(Integer, ForeignKey('food.id'), nullable=False, comment='食物ID')
    quantity = Column(Integer, nullable=False, comment='食物数量')
