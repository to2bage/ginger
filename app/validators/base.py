"""
  *@ClassName base
  *@Description TODO
  *@Author to2bage
  *@Date 2020-07-26 15:18
  *@Version 1.0
 """
from wtforms import Form
from flask import request

from app.libs.error_code import ParameterException

class BaseForm(Form):
    def __init__(self):
        super().__init__(data=request.json)

    def validate_for_api(self):
        valid = super().validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self

    pass