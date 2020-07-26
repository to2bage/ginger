"""
  *@ClassName forms
  *@Description TODO  校验Form
  *@Author to2bage
  *@Date 2020-07-26 11:18
  *@Version 1.0
 """
from wtforms import StringField, IntegerField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form):
    account = StringField(
        validators=[
            DataRequired(message="account是必填项目"),
            Length(min=5, max=32, message="account的长度必须介于[5,32]")
        ]
    )
    secret = StringField(
        validators=[

        ]
    )
    # 客户端类型
    type = IntegerField(
        validators=[
            DataRequired(message="type是必填项目")
        ]
    )

    # 自定义验证器, value不是用户传递过来的数字, 所以必须通过value.data获得
    def validate_type(self, value):
        try:
            client_type = ClientTypeEnum(value.data)
        except Exception as err:
            raise ValidationError("type必须是指定的内容...")


class UserEmailForm(ClientForm):
    account = StringField(
        validators=[
            Email(message="email格式不正确")
        ]
    )
    secret = StringField(
        validators=[
            DataRequired(message="密码是必填项目"),
            Regexp(r"^[a-zA-Z0-9_*&$#@]{6,22}$")
        ]
    )
    nickname = StringField(
        validators=[
            DataRequired(message="nickname是必填项目"),
            Length(min=2, max=22)
        ]
    )

    def validate_account(self, value):
        # value.data是否存在于数据库
        if User.query.filter_by(email=value.data).first():
            raise ValidationError(f"{value.data}已经存在")
