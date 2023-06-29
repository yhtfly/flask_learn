from flask import request,jsonify,session,Blueprint
from . import app
from .models import User,Admin,db


#创建蓝图对象
admin = Blueprint("admin",__name__)
user = Blueprint("user",__name__)

@user.route('/index')
def hello_user():
    return 'Hello World! user!'

@admin.route('/index')
def hello_admin():
    return "Hello World! admin!"

#用户注册
@user.route("/register",methods=["POST"])
def user_register():
    try:
        data = request.get_json()
        print(data)
        username = data.get("username")
        password = data.get("password")
        if not all([username,password]):
            return jsonify(msg="参数不完整",code=4000)
        user = User(username=username,password=password)
        try:
            db.session.add(user)
            db.session.commit()
            return jsonify(code=200,msg="注册成功",username=username)
        except Exception as e:
            print(e)
            return jsonify(msg="存数据库失败",code=4001)
    except Exception as e:
        print(e)
        return jsonify(msg="出错了哦，请查看是否正确访问",code=4002)

#用户登录
@user.route('/login',methods=["POST"])
def user_login():
    get_data = request.get_json()
    username = get_data.get("username")
    password = get_data.get("password")



    if not all([username,password]):
        return jsonify(msg="参数不完整",code=4000)

    user =User.query.filter(User.username==username).first()

    if user and user.password == password:
        session[username] = username
        print(session[username])
        return jsonify(msg="登录成功",code=200,username=username,sid=session.sid)
    else:
        return jsonify(msg="用户名或密码错误",code=4001)


#用户登出
@user.route("/logout/<username>",methods=["GET"])
def user_logout(username):
    username = session.get(username)
    if username is None:
        return jsonify(msg="出错了，没登录！",code=4000)
    session.pop(username)
    return jsonify(msg="成功退出登录！",code=200)



#管理员注册
@admin.route("/register",methods=["POST"])
def admin_register():
    try:
        data = request.get_json()
        print(data)
        username = data.get("username")
        password = data.get("password")
        if not all([username,password]):
            return jsonify(msg="参数不完整",code=4000)
        admin = Admin(username=username,password=password)
        try:
            db.session.add(admin)
            db.session.commit()
            return jsonify(code=200,msg="注册成功",username=username)
        except Exception as e:
            print(e)
            return jsonify(msg="存数据库失败",code=4001)
    except Exception as e:
        print(e)
        return jsonify(msg="出错了哦，请查看是否正确访问",code=4002)

#管理员登录
@admin.route('/login',methods=["POST"])
def admin_login():
    get_data = request.get_json()
    username = get_data.get("username")
    password = get_data.get("password")



    if not all([username,password]):
        return jsonify(msg="参数不完整",code=4000)

    admin =Admin.query.filter(Admin.username==username).first()

    if admin and admin.password == password:
        session[username] = username
        print(session[username])
        return jsonify(msg="登录成功",code=200,username=username,sid=session.sid)
    else:
        return jsonify(msg="用户名或密码错误",code=4001)


# 检查登录状态
@app.route("/session/<username>",methods=["GET"])
def check_session(username):
    username = session.get(username)
    if username is not None:
        return jsonify(username=username,code=200,sid=session.sid)
    else:
        return jsonify(msg="出错了，没登录",code=4000)


# 登出
@admin.route("/logout/<username>",methods=["GET"])
def admin_logout(username):
    username = session.get(username)
    if username is None:
        return jsonify(msg="出错了，没登录！",code=4000)
    session.pop(username)
    return jsonify(msg="成功退出登录！",code=200)
