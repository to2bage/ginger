"""
  *@ClassName app
  *@Description TODO 所有与flask核心对象初始化, 和相关的操作
  *@Author to2bage
  *@Date 2020-07-26 10:10
  *@Version 1.0
 """
from flask import Flask

from app.api.v1 import create_blueprint_v1
from app.models.bases import db


def create_app():
    app = Flask(__name__)

    app.config.from_object("app.config.secret")
    app.config.from_object("app.config.settings")

    register_blueprint(app)

    register_plugin(app)        #  插件的注册

    return app


def register_blueprint(app):
    bp_v1 = create_blueprint_v1()
    app.register_blueprint(bp_v1, url_prefix="/v1")


def register_plugin(app: Flask):
    db.init_app(app)

    with app.app_context():
        db.create_all()
