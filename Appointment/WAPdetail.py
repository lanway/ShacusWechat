# -*-coding:utf-8 -*-
'''
@author :兰威
@type：微信的约拍详情
@datatime：2016.10.25
'''
import json

from  BaseHandlerh import BaseHandler
from Database.tables import WAppointEntry, WAppointment, WApImage, User
from WAPmodel import WAPmodel

class WAPdetail(BaseHandler):

    retjson = {'code': '400', 'contents': 'None'}
    def get(self):

        phone = self.get_argument('phone')
        m_apid = self.get_argument('apid')

        isregist = 0
        issponsor = 0
        wap_pic = []
        wapmodel = WAPmodel()
        try:
            user = self.db.query(User).filter(User.Utel == phone).one()
            m_id = user.Uid
            date = self.db.query(WAppointEntry).filter(WAppointEntry.WAEapid == m_apid,WAppointEntry.WAEvalid == 1).all()
            for item in date:
                if item.WAEregisterID == int(m_id):
                    isregist =1
                    break
            wap = self.db.query(WAppointment).filter(WAppointment.WAPid == m_apid,WAppointment.WAPvalid == 1).one()
            if wap.WAPsponsorid == int(m_id):
                issponsor = 1
            wap_picturls = self.db.query(WApImage).filter(WApImage.WAPIapid == m_apid).all()
            for pic in wap_picturls:
                wap_pic.append(pic.WAPIurl)
            retdate = wapmodel.wap_model_mutiple(wap,wap_pic,issponsor,isregist)
            self.retjson['contents'] = retdate
            self.retjson['code'] = '10401'
        except Exception,e:
            print e
            self.retjson['contents'] = "该活动无效"
            self.retjson['code'] = '10400'
        callback = self.get_argument("jsoncallback")
        jsonp = "{jsfunc}({json});".format(jsfunc=callback, json=json.dumps(self.retjson, ensure_ascii=False, indent=2))
        self.write(jsonp)

