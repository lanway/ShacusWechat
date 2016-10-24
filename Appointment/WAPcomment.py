# -*- coding:utf-8 -*-
'''
@author:黄鑫晨
@name:约拍评论处理
@time:2016-10-24
'''
import json

from BaseHandlerh import BaseHandler
from Database.tables import WApInfo

class APcommentHandler(BaseHandler):
    '''
    对约拍的评论进行处理
    '''
    retjson = {'code':'','contents':''}

    def commit(self):
        try:
            self.db.commit()
        except Exception,e:
            self.retjson['code'] = u'500'
            self.retjson['contents'] = u"数据库提交错误"

    def post(self):
        apid = self.get_argument("apid")  # 约拍id
        uid = self.get_argument("uid")  # 评论用户的id
        try:
            # 约拍项
            ap_info_entry = self.db.query(WApInfo).filter(WApInfo.WAIappoid == apid, WApInfo.WAIvalid == 1).one()
            try:
                score = self.get_argument("score") # 评分
                try:
                    comment = self.get_argument("comment")  # 评论
                except Exception, e:
                    print e
                # 模特评论摄影师
                if uid == ap_info_entry.WAImid:
                    ap_info_entry.WAIpscore = score
                    if comment:
                        ap_info_entry.WAImcomment = comment
                    self.commit()
                # 摄影师评论模特
                elif uid == ap_info_entry.WAIpid:
                    ap_info_entry.WAImscore = score
                    if comment:
                        ap_info_entry.WAIpcomment = comment
                    self.commit()
                # 用户Id不在该约拍中
                else:
                    self.retjson['code'] = u'40002'
                    self.retjson['contents'] = u'该用户未参加此次约拍'
            except Exception, e:
                print e
        except Exception,e:
            self.retjson['code'] = u'40001'
            self.retjson['contents'] = u"该约拍项不存在或已失效"
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))


