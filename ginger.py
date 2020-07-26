"""
  *@ClassName ginger
  *@Description TODO   入口文件
  *@Author to2bage
  *@Date 2020-07-26 10:15
  *@Version 1.0
 """
from werkzeug.exceptions import HTTPException

from app.app import create_app
from app.libs.error import APIException

app = create_app()

# 在入口文件处, 捕捉所有未知的异常
@app.errorhandler(Exception)
def framework_error(e):
    # 只有在flask1.0的版本中, 才能捕捉到所有的异常
    if isinstance(e, APIException):
        return e
    elif isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 10007
        return APIException(msg, code, error_code)
    else:
        return APIException()
    pass


if __name__ == '__main__':
    app.run()
