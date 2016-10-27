#-*- coding:utf-8 -*-

'''
@王佳镭
@2016.10.26
'''
import json

from sqlalchemy import desc


from BaseHandlerh import  BaseHandler
from Database.tables import WActivity, User, WAcImage, UserImage, Image, WAcEntry
from Activity.WAcmodel import ACmodelHandler

class UserAclist(BaseHandler): #关于用户的一系列活动
    retjson = {'code': '400', 'contents': 'none'}
    def get(self):
        u_phone= self.get_argument('id')
        try:
            u_id = self.db.query(User).filter(User.Utel == u_phone).one()
            try:
                data = self.db.query(WAcEntry).filter(WAcEntry.WACEregisterid == u_id.Uid).all()
                for Ac1 in data:
                    ac = self.db.query(WActivity).filter(Ac1.WACEacid == WActivity.WACid).all()
                retdata = []
                for item in ac:
                    retdata01 = ACmodelHandler.ac_Model_simply(item, retdata)
                    self.retjson['code'] = '10600'
                    retdata.append(retdata01)
                self.retjson['contents'] = retdata
            except Exception, e:
                print e
                self.retjson['code'] = '10601'
                self.retjson['contents'] = '你还没有参加过任何活动'
        except Exception, e:
            print e
            self.retjson['code'] = '10604'
            self.retjson['contents'] = '没有此用户'
        callback = self.get_argument("jsoncallback")
        jsonp = "{jsfunc}({json});".format(jsfunc=callback, json=json.dumps(self.retjson, ensure_ascii=False, indent=2))
        self.write(jsonp)