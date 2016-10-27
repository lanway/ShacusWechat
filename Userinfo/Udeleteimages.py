# -*— coding:utf-8 -*-
'''
author:wjl
'''
from BaseHandlerh import BaseHandler
from Database.tables import User, WAppointment, Homepageimage
from FileHandler.ImageHandler import ImageHandler
from Userinfo.UserImgHandler import UserImgHandler
from Wechatserver.Wpichandler import Wpichandler

class Uaddimages(BaseHandler):#用户在个人主页删除照片
    retjson={'code':'200','contents':'null'}
    def get(self):
        u_phone = self.get_argument('phone')
        images = self.get_argument('images')
        retimages = []
        for i in images:
            user = self.db.query(Homepageimage).filter(Homepageimage.HPuser == u_phone and Homepageimage.HPimgurl==images).all()
            retimages.append(user)
        if retimages:
            for item in retimages:
                item.HPimgvalid = False
                self.db.commit()
                self.retjson['contents']='删除图片成功'