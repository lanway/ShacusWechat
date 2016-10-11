# coding=utf-8
import json

from tornado.escape import json_encode

from BaseHandlerh import BaseHandler
from Database.tables import WActivity

'''
@author:黄鑫晨
@2016-10-11
@返回活动详细信息
'''

class AcInfoHandler(BaseHandler):
    retjson = {'code': '10300', 'contents': 'None'}

    def post(self):
        acid = self.get_argument('acid')  # 活动id
        # 判断是否有权限
        try:
            exist = self.db.query(WActivity).filter(WActivity.WACid == acid, WActivity.WACvalid==1).one()
            # 该活动存在
            if exist:
                activity = dict(
                    id=exist.WACid,
                    sponsorid=exist.WACsponsorid,
                    location=exist.WAClocation,
                    title=exist.WACtitle,
                    startT=exist.WACstartT.strftime('%Y-%m-%d %H:%M:%S'),
                    endT=exist.WACendT.strftime('%Y-%m-%d %H:%M:%S'),
                    joinT=exist.WACjoinT.strftime('%Y-%m-%d %H:%M:%S'),
                    content=exist.WACcontent,
                    free=exist.WACfree,
                    price=exist.WACprice,
                    closed=exist.WACclosed,
                    createT=exist.WACcreateT.strftime('%Y-%m-%d %H:%M:%S'),
                    maxp=exist.WACmaxp,
                    minp=exist.WACminp,
                    registN=exist.WACregistN,
                    status=exist.WACstatus,
                )
                self.retjson['contents'] = activity
        except Exception, e:
            print e
            self.retjson['code'] = '402'
            self.retjson['contents'] = '该活动不存在或已失效'
        callback = self.get_argument("jsoncallback")
        jsonp = "{jsfunc}({json});".format(jsfunc=callback, json=json.dumps(self.retjson, ensure_ascii=False, indent=2))
        self.write(jsonp)
