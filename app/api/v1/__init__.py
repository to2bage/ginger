"""
  *@ClassName __init__.py
  *@Description TODO
  *@Author to2bage
  *@Date 2020-07-26 10:20
  *@Version 1.0
 """
from flask import Blueprint

from app.api.v1 import user
from app.api.v1 import client


def create_blueprint_v1():
    bp_v1 = Blueprint("v1", __name__)

    # 宏图 注册到 蓝图
    # user.api.register(bp_v1, url_prefix="/user")
    user.api.register(bp_v1)
    client.api.register(bp_v1)

    return bp_v1
