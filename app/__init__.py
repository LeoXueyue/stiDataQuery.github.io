from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#jinja2模板格式转换:年月日时分秒转年月日
def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)

app = Flask(__name__)
#数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin123456@168.160.61.157/sti'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SECRET_KEY'] = '38cf131a683246118b57b47bc5f2b481'

db = SQLAlchemy(app)
app.debug = True

app.jinja_env.filters['datetime'] = datetimeformat

#蓝图注册
from app.admin import admin as admin_blueprint

app.register_blueprint(admin_blueprint,url_prefix="/admin")