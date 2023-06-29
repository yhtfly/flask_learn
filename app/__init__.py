from flask import Flask,request,jsonify,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import redis

app = Flask(__name__)

#数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:test@127.0.0.1:3306/cainiao'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "uowfuosdiofjisdfjoisdfjo"

#session配置
app.config["SESSION_TYPE"]="redis"
app.config["SESSION_USE_SIGNER"]=True #对cookie中session_id进行隐藏处理
app.config["PERMANENT_SESSION_LIFETIME"]=1000 #session数据的有效期，单位秒
app.config['SESSION_REDIS']=redis.Redis(host='49.232.7.27',port=6379,password="he123",db=1)


db = SQLAlchemy(app)

#实例化migrate对象
migrate = Migrate(app, db)


from flask_session import Session
Session(app)

# 注册蓝图
from .api import user,admin  # 导入包

app.register_blueprint(user, url_prefix="/user")  # 绑定包里面的蓝图对象
app.register_blueprint(admin, url_prefix="/admin")