"""
  *@ClassName user
  *@Description TODO 关于User的视图函数  127.0.0.1:5000/v1/user/get
  *@Author to2bage
  *@Date 2020-07-26 10:20
  *@Version 1.0
 """


from app.libs.redprint import Redprint


api = Redprint("user")

@api.route("/get")
def get_user():
    return " i am totobage"