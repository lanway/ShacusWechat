# -*-coding:utf-8 -*-
'''
@author :兰威
@type：微信的约拍选择报名用户
@datatime：2016.10.26
'''
from BaseHandlerh import BaseHandler
from Database.tables import User


class WAPselect(BaseHandler):

    def get(self):

        phone = self.get_argument('phone')
        r_id = self.get_argument('registid')
        ap_id = self.get_argument("apid")

        uid = self.db.query(User).filter(User.Utel == phone).one()
        try:
            exist = self.db.query()
