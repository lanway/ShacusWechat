# -*- coding:utf-8 -*-
'''
   @兰威
   @datatime：2016.10.10
   @type：回复约拍列表
'''
import json

from BaseHandlerh import BaseHandler
import sys
sys.path.append("..")
from Database.tables import WAppointment, WApImage
from WAPmodel import WAPmodel

class WAPList(BaseHandler):

    retjson = {'code': '', 'contents': ''}
    def get(self):

        try:
            wapmodel = WAPmodel()
            waps = self.db.query(WAppointment).filter(WAppointment.WAPstatus == 0,WAppointment.WAPvalid == 1).order_by(WAppointment.WAPcreateT).limit(10).all()
            picurls = []
            for wap in waps:
                data = self.db.query(WApImage).filter(WApImage.WAPIapid == wap.WAPid).all()
                picurls.append(data[0].WAPIurl)
            retdata =  wapmodel.wap_model_simply_more(waps,picurls)
            self.retjson['code'] = '10210'
            self.retjson['contents'] = retdata


        except Exception,e:
            self.retjson['code'] = '10211'
            self.retjson['contents'] = '服务器错误'
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))




