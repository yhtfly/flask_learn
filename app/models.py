from . import db


#用户表
class User(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),nullable=False,unique=True)
    password = db.Column(db.String(64),nullable=False)
    phone=db.Column(db.String(11))
    address=db.Column(db.String(11))

#管理员表
class Admin(db.Model):
    __tablename__="admin"
    id= db.Column(db.Integer,primary_key=True)
    username =db.Column(db.String(64),nullable=False,unique=True)
    password =db.Column(db.String(64),nullable=False)
    power=db.Column(db.Enum("管理员","超级管理员"),nullable=False,default="管理员")
    phone=db.Column(db.String(11))
    address=db.Column(db.String(11))