# coding=utf-8
import base64
import json
from Database.tables import  User, WAcEntry

'''
@author:兰威
'''
from BaseHandlerh import  BaseHandler
from Userinfo.Usermodel import wechat_user_model_simply
class WAcseeregist(BaseHandler):

    '''
    查看报名用户
    '''
    retjson = {'code':'','contents':''}
    def get(self):

        acid = self.get_argument('acid')
        m_phone = self.get_argument('phone')

        try:
            u_id = self.db.query(User).filter(User.Utel == m_phone).one()
            data = self.db.query(WAcEntry).filter(WAcEntry.WACEid == acid,WAcEntry.WACEregistvalid == 1).all()
            retdata = []
            for item in data:
                userid = item.WACEregisterid
                user = self.db.query(User).filter(User.Uid == userid).one()
                retdata_item = wechat_user_model_simply(user)
                retdata.append(retdata_item)
            self.retjson['code'] = '10400'
            self.retjson['contents'] = retdata



        except Exception,e:
            print e
            self.retjson['code'] = '10400'
            self.retjson['contents'] = '用户不存在'
        callback = self.get_argument("jsoncallback")
        jsonp = "{jsfunc}({json});".format(jsfunc=callback, json=json.dumps(self.retjson, ensure_ascii=False, indent=2))
        self.write(jsonp)


