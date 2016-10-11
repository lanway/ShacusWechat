#-*- coding:utf-8 -*-

'''
@王佳镭
@2016.9.3
'''
import json

from sqlalchemy import desc


from BaseHandlerh import  BaseHandler
from Database.tables import WActivity, User, WAcImage, UserImage, Image
from Activity.WAcmodel import ACmodelHandler

class AskActivity(BaseHandler): #关于用户的一系列活动
    retjson = {'code': '200', 'contents': 'none'}
    def post(self):
            try:
                data = self.db.query(WActivity).filter(WActivity.WACvalid == 1).order_by(desc(WActivity.WACcreateT)).limit(5).all()
                retdata = []
                for item in data:
                        ACmodelHandler.ac_Model_simply(item,retdata)
                        self.retjson['code'] = '10303'
                        self.retjson['contents'] = retdata
            except Exception,e:
                print e
                self.retjson['code']= '10304'
                self.retjson['contents']='there is no activity'