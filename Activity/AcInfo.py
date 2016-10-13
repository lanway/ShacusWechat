# coding=utf-8
import json

from tornado.escape import json_encode

from BaseHandlerh import BaseHandler
from Database.tables import WActivity, WAcImage, User, WAcEntry
from FileHandler.Upload import AuthKeyHandler

'''
@author:黄鑫晨
@2016-10-11
@返回活动详细信息
'''

class AcInfoHandler(BaseHandler):
    retjson = {}

    def get(self):
        acid = self.get_argument('acid')  # 活动id
        m_phone = self.get_argument('phone') #用户手机
        userinfo = self.db.query(User).filter(User.Utel == m_phone).one()  # 判断是否报名
        isregist = 0
        try:
            acregist = self.db.query(WAcEntry).filter(
                WAcEntry.WACEacid == acid and WAcEntry.WACEregisterid == m_phone).one()
            if acregist.WACEregistvalid == 1:
                isregist = 1
            elif acregist.WACEregistvalid == 0:
                isregist = 0
        except Exception, e:
            isregist = 0
            print "没有报名"




        # 判断是否有权限
        auth  = AuthKeyHandler()

        try:
            exist = self.db.query(WActivity).filter(WActivity.WACid == acid, WActivity.WACvalid == 1).one()
            # 该活动存在
            if exist:
                picurls = []
                pics = self.db.query(WAcImage).filter(WAcImage.WACIacid == acid).all()
                for pic in pics:
                    picurls.append(auth.download_url(pic.WACIurl))



                activity = dict(
                    code=200,
                    id=exist.WACid,
                    sponsorid=exist.WACsponsorid,
                    isregist = isregist,
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
                    picurls=picurls,
                )
                self.retjson = activity
        except Exception, e:
            print e
            self.retjson['contents'] = dict(
                code=402,
                content='该活动不存在或已失效')
        callback = self.get_argument("jsoncallback")
        jsonp = "{jsfunc}({json});".format(jsfunc=callback, json=json.dumps(self.retjson, ensure_ascii=False, indent=2))
        self.write(jsonp)
