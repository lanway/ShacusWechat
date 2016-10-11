# coding=utf-8
import json
from Database.tables import UserImage, Image,WActivity, WAcImage, User, WAcEntry
from FileHandler.Upload import AuthKeyHandler
from Database.models import get_db
from BaseHandlerh import BaseHandler
'''
@author:王佳镭
'''
class WAcregist(BaseHandler):
    retjson= {'code':'200','contents':'null'}
    def get(self):
        m_wacid = self.get_argument('wacid',default='null')
        m_phone = self.get_argument('phone',default='null')
        try:
            userinfo = self.db.query(User).filter(User.Utel==m_phone).one()
            userid = userinfo.Uid
            try:
                acregist = self.db.query(WAcEntry).filter(WAcEntry.WACEacid == m_wacid and WAcEntry.WACEregisterid == m_phone).one()
                if acregist:
                    if acregist.WACEregistvalid == 1:
                        self.retjson['contents'] = '10307'
                        self.retjson['contents'] = '已经报名'
                    elif acregist.WACEregistvalid == 0:
                        acregist.WACEregistvalid = 1
                        self.db.commit()
                        self.retjson['code']  = '10306'
                        self.retjson['contents']= '报名成功'
            except Exception,e:
                print e
                new_acregist = WAcEntry(
                    WACEacid=m_wacid,
                WACEregisterid = userid,
                WACEregistvalid = 1,
                )
                self.db.merge(new_acregist)
                try:
                    self.db.commit()
                    self.retjson['code'] = '10312'
                    self.retjson['contents'] = '报名成功'
                except Exception, e:
                    self.db.roolback()
                    self.retjson['code'] = '10305'
                    self.retjson['contents'] = '服务器错误'
        except Exception,e:
            print e
            self.retjson['contents'] = '10308'
            self.retjson['contents'] = '没有此用户'
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))