# coding=utf-8
'''
@author: 黄鑫晨
'''
import json

import tornado
from sqlalchemy import desc
from tornado import gen
from tornado.concurrent import Future
from tornado.web import asynchronous

from BaseHandlerh import BaseHandler
from Database.tables import  User
from Userinfo import Usermodel
from Userinfo.Ufuncs import Ufuncs
from Userinfo.Usermodel import Model_daohanglan

class WLoginHandler(BaseHandler):

    retjson = {'code': '', 'contents': u'未处理 '}



    @asynchronous
    @gen.coroutine
    def post(self):

        m_phone = self.get_argument('phone')
        m_password = self.get_argument('password')
        if not m_phone or not m_password:
            self.retjson['code'] = 400
            self.retjson['contents'] = 10105  # '用户名密码不能为空'
        #todo:登录返回json的retdata多一层[]，客户端多0.5秒处理时间
        # 防止重复注册
        else:
            try:
                user = self.db.query(User).filter(User.Utel == m_phone).one()
                if user:  # 用户存在
                    password = user.Upassword
                    if m_password == password:  # 密码正确
                        self.get_login_model(user)
                    else:
                        self.retjson['contents'] = u'密码错误'
                        self.retjson['code'] = '10114'  # 密码错误
                else:  # 用户不存在
                    self.retjson['contents'] = u'该用户不存在'
                    self.retjson['code'] = '10113'
            except Exception, e:  # 还没有注册
                print "异常："
                print e
                self.retjson['contents'] = u'该用户名不存在'
                self.retjson['code'] = '10113'  # '该用户名不存在'



    @asynchronous
    @gen.coroutine
    def get_login_model(self, user):
        retdata = []
        user_model = Usermodel.get_user_detail_from_user(user)  # 用户模型
        photo_list = []  # 摄影师发布的约拍
        model_list = []
        try:
            photo_list_all = self.db.query(Appointment).filter(Appointment.APtype == 1,
                                                               Appointment.APvalid == 1). \
                order_by(desc(Appointment.APcreateT)).limit(6).all()
            model_list_all = self.db.query(Appointment).filter(Appointment.APtype == 0,
                                                               Appointment.APvalid == 1). \
                order_by(desc(Appointment.APcreateT)).limit(6).all()
            from Appointment.APmodel import APmodelHandler
            ap_model_handler = APmodelHandler()  # 创建对象

            ap_model_handler.ap_Model_simply(photo_list_all, photo_list, user.Uid)
            ap_model_handler.ap_Model_simply(model_list_all, model_list, user.Uid)
            data = dict(
                userModel=user_model,
                daohanglan=self.bannerinit(),
                photoList=photo_list,
                modelList=model_list,
            )

            retdata.append(data)
            self.retjson['code'] = '10111'
            self.retjson['contents'] = retdata
        except Exception, e:
            print e
            self.retjson['contents'] = r"摄影师约拍列表导入失败！"