#-*- coding:utf-8 -*-

'''
@王佳镭
@2016.10.26
'''
import json

from sqlalchemy import desc


from BaseHandlerh import  BaseHandler
from Database.tables import WActivity, User, WAcImage, UserImage, Image, WAcEntry, WAppointEntry, WApImage, WAppointment
from Appointment.WAPmodel import WAPmodel
from FileHandler.Upload import AuthKeyHandler



class UserAplist(BaseHandler): #关于用户的一系列活动
    retjson = {'code': '400', 'contents': 'none'}
    def get(self):
        u_phone = self.get_argument('phone')
        try:
            userinfo = self.db.query(User).filter(User.Utel==u_phone).one()
            try:
                data = self.db.query(WAppointEntry).filter(WAppointEntry.WAEregisterID == userinfo.Uid).all()
                for item02 in data:
                    ap = self.db.query(WAppointment).filter(item02.WAEapid == WAppointment.WAPid)
                retdata = []
                auth = AuthKeyHandler()
                wapmodel = WAPmodel()
                for item in ap:
                    aplurl = self.db.query(WApImage).filter(WApImage.WAPIapid == item.WAPid).all()
                    APurl = auth.download_url(aplurl[0].WAPIurl)
                    retdata01 = wapmodel.wap_model_simply_one(item ,APurl)
                    self.retjson['code'] = '10602'
                    retdata.append(retdata01)
                self.retjson['contents'] = retdata
            except Exception, e:
                print e
                self.retjson['code'] = '10603'
                self.retjson['contents'] = '你还没有参加过任何约拍'
        except Exception, e:
            print e
            self.retjson['code']='10604'
            self.retjson['contents']='没有此用户'
        callback = self.get_argument("jsoncallback")
        jsonp = "{jsfunc}({json});".format(jsfunc=callback, json=json.dumps(self.retjson, ensure_ascii=False, indent=2))
        self.write(jsonp)