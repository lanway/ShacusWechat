# -*-coding:utf-8 -*-
'''
@author :兰威
@type：微信的约拍选择报名用户
@datatime：2016.10.26
'''
from BaseHandlerh import BaseHandler
from Database.tables import User, WApInfo


class WAPselect(BaseHandler):

    retjson = {'code': '', "contents": ''}
    def get(self):

        phone = self.get_argument('phone')
        r_id = self.get_argument('registid')
        ap_id = self.get_argument("apid")
        type = self.get_argument('type')

        uid = self.db.query(User).filter(User.Utel == phone).one()
        try:
            exist = self.db.query(WApInfo).filter(WApInfo.WAIappoid == ap_id).one()
            self.retjson['code'] = '10291'
            self.retjson['contents'] = '此约拍已经选择'
        except Exception,e:
            print e
            new_item = dict(


            )
