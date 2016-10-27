# -*— coding:utf-8 -*-
'''
author:wjl
'''
from BaseHandlerh import BaseHandler
from Database.tables import User, WAppointment
from FileHandler.ImageHandler import ImageHandler
from Userinfo.UserImgHandler import UserImgHandler
from Wechatserver.Wpichandler import Wpichandler

class Uaddimages(BaseHandler):#用户在个人主页增加图片
    retjson={'code':'200','contents':'none'}
    def get(self):
        u_phone = self.get_argument('phone')
        images = self.get_argument('image')
        wpicture = Wpichandler()
        image =UserImgHandler()
        if wpicture.pichandler(images,images):
            image.insert_Homepage_image(images,u_phone)

            self.db.commit()
            self.retjson['contents'] = '上传主页图片成功'



