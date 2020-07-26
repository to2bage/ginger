"""
  *@ClassName error_code
  *@Description TODO 自定义异常
  *@Author to2bage
  *@Date 2020-07-26 13:56
  *@Version 1.0
  400: 请求参数错误
  401: 未授权
  403: 禁止访问
  404: 没有找到资源
  500: 服务器的内部错误
  200: 查询成功
  201: 创建/更新成功
  204: 删除成功
  301: 重定向
 """
from app.libs.error import APIException


class Success(APIException):
    code = 200
    msg = "Congratulations!!!"
    error_code = 0

class ClientTypeError(APIException):
    code = 400
    msg = "client is invalid"
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = "invalid parameter"
    error_code = 1000