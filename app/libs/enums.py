"""
  *@ClassName enums
  *@Description TODO
  *@Author to2bage
  *@Date 2020-07-26 11:14
  *@Version 1.0
 """
from enum import Enum


class ClientTypeEnum(Enum):
    # 客户端的类型
    USER_EMAIL = 100
    USER_MOBILE = 101

    USER_MINA = 200
    USER_WX = 201
    pass
