"""
  *@ClassName client
  *@Description TODO    客户端的视图函数
  *@Author to2bage
  *@Date 2020-07-26 11:10
  *@Version 1.0
 """
from flask import request

from app.libs.redprint import Redprint
from app.validators.forms import ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.libs.error_code import ClientTypeError
from app.libs.error_code import Success

api = Redprint("client")


# 127.0.0.1:5000/v1/client/register
@api.route("/register", methods=["POST"])
def create_client():
    """
    :return:
    客户端 注册 """
    # 校验客户端的数据, 使用app.validators.forms.py
    # data = request.json     # 接受数据, 必须是data=data
    # data = request.args.to_dict()

    # form = ClientForm(data=data)    # 使用自定义的校验ClientForm校验数据

    # if form.validate():
    #     promise = {
    #         ClientTypeEnum.USER_EMAIL: __register_user_by_email
    #     }
    #     # print(form.account.data)
    #     # print(form.secret.data)
    #     # print(form.type.data)     #  100
    #     promise[ClientTypeEnum(form.type.data)]()           # 调用相应的方法
    # else:
    #     print(form.errors)
    #     raise ClientTypeError()

    form = ClientForm().validate_for_api()

    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[ClientTypeEnum(form.type.data)]()

    return Success()


def __register_user_by_email():
    # form = UserEmailForm(data=request.json)
    # if form.validate():
    #     # print(form.nickname.data)
    #     # print(form.account.data)
    #     # print(form.secret.data)
    #     # print(form.type.data)
    #     User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
    # else:
    #     # 验证不成功, 这里要抛出异常
    #     # print(form.errors)
    #     # raise ClientTypeError()
    #     pass
    #
    form = UserEmailForm().validate_for_api()

    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
    pass
