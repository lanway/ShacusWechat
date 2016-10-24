# -* coding:utf-8 *-
'''
@author:黄鑫晨
@time：2016-10-24
@introduce：返回用户个人信息
'''
import json

from BaseHandlerh import BaseHandler
from Database.tables import User, WApInfo


class UHandler(BaseHandler):
    retjson = {'code': '', 'sign': '','comments':''}

    def post(self):
        type = self.get_argument('type')
        # 请求用户自己的个人主页
        if type == '1':
            openid = self.get_argument('openid')
            try:
                user = self.db.query(User).filter(User.Uopenid == openid).one()
                uid = user.Uid
                sign = user.Usign
                if sign:
                    self.retjson['sign'] = sign
                # 获得用户的评论
                comments = []
                try:
                    # 用户作为摄影师参加的约拍
                    asphotoers = self.db.query(WApInfo).filter(WApInfo.WAIpid == uid).all()
                    for each in asphotoers:
                        # 模特对摄影师的评论
                        if each.WAImcomment:
                            comment = each.WAImcomment
                            comments.append(comment)
                except Exception, e:
                    print e
                try:
                    # 用户作为模特参加的约拍
                    asmodels = self.db.query(WApInfo).filter(WApInfo.WAImid == uid).all()
                    for each in asmodels:
                        # 摄影师对模特的评论:
                        if each.WAIpcomment:
                            comment = each.WAIpcomment
                            comments.append(comment)
                except Exception, e:
                    print e
                if comments:
                    self.retjson['comments'] = comments
            except Exception, e:
                print e
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))



