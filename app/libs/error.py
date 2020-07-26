"""
  *@ClassName error
  *@Description TODO
  *@Author to2bage
  *@Date 2020-07-26 14:14
  *@Version 1.0
  error_code 999 未知错误
 """
from werkzeug.exceptions import HTTPException
from flask import request, json


class APIException(HTTPException):
    code = 500
    msg = "Sorry, we make a mistake 囧rz ( ◑ٹ◐)"
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        super().__init__(msg, None)
        if code is not None:
            self.code = code
        if msg:
            self.msg = msg
        if error_code:
            self.error_code = error_code

    def get_body(self, environ=None):
        # body: 错误信息的json格式
        body = dict(
            msg = self.msg,
            error_code = self.error_code,
            request = f"{request.method} {APIException.get_url_no_param()}"
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [("Content-Type", "application/json; charset=utf-8")]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split("?")
        return main_path[0]