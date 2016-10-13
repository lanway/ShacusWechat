# coding=utf-8
import base64
import json
from Database.tables import  User
'''
@author:兰威
'''
from BaseHandlerh import  BaseHandler

class WAcseeregist(BaseHandler):

    '''
    查看报名用户
    '''
    retjson = {'code':'','contents':''}
    def get(self):

        acid = self.get_argument('acid')
        m_phone = self.get_argument('phone')

        m_phone  = base64.encodestring(m_phone)
        try:
            u_id = self.db.query(User).filter(User.Utel == m_phone).one()
        except Exception,e:
            print e
            self.retjson['code'] = '10400'
            self.retjson['contents'] = '用户不存在'


