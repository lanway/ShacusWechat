# -* coding:utf-8 *-
'''
@author:黄鑫晨
@time：2016-10-24
@introduce：返回用户个人信息
'''
import json

from BaseHandlerh import BaseHandler
from Database.tables import User, WApInfo, WAppointment


class UHandler(BaseHandler):
    retjson = {'code': '', 'sign': '','comments':'','contents':''}

    def post(self):
        type = self.get_argument('type')
        # 请求用户自己的个人主页
        if type == '1':
            # openid = self.get_argument('openid')
            utel = self.get_argument('utel')
            try:
                #user = self.db.query(User).filter(User.Uopenid == openid).one()
                user = self.db.query(User).filter(User.Utel == utel).one()
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
                            comment_content = each.WAImcomment
                            score = each.WAIpscore  # 摄影师获得的评分
                            comment_user_id = each.WAImid  # 模特的id
                            apid = each.WAIappoid

                            try:
                                model = self.db.query(User).filter(User.Uid == comment_user_id).one()
                                appointment = self.db.query(WAppointment).filter(WAppointment.WAPid == apid ).one()
                                ap_name = appointment.WAPtitle
                                model_name = model.Ualais
                                comment_entry = dict(
                                    comment=comment_content,
                                    alais=model_name,
                                    score=score,
                                    title=ap_name
                                )
                                comments.append(comment_entry)
                                self.retjson['code'] = '200'
                                self.retjson['contents'] = u"成功"
                            except Exception, e:
                                self.retjson['code'] = u'40005'
                                self.retjson['contents'] = u"获取评论用户出错"
                except Exception, e:
                    print e
                self.retjson['code'] = u'40002'
                self.retjson['contents'] = u"该用户作为摄影师没有发布过约拍"
                try:
                    # 用户作为模特参加的约拍
                    asmodels = self.db.query(WApInfo).filter(WApInfo.WAImid == uid).all()
                    for each in asmodels:
                        # 摄影师对模特的评论:
                        if each.WAIpcomment:
                            comment_content = each.WAIpcomment
                            comment_user_id = each.WAIpid  # 摄影师的id
                            score = each.WAImscore  # 模特获得的评分
                            try:
                                photoer = self.db.query(User).filter(User.Uid == comment_user_id).one()
                                photoer_name = photoer.Ualais
                                comment_entry = dict(
                                    comment=comment_content,
                                    alais=photoer_name,
                                    score=score
                                )
                                comments.append(comment_entry)
                                self.retjson['code'] = '200'
                                self.retjson['contents'] = u"成功"
                            except Exception,e:
                                self.retjson['code'] = '40005'
                                self.retjson['contents'] = u"获取评论用户出错"
                except Exception, e:
                    print e
                    self.retjson['code'] = u'40003'
                    self.retjson['contents'] = u"该用户作为模特没有发布过约拍"
                if comments:
                    self.retjson['comments'] = comments
            except Exception, e:
                print e
            self.retjson['code'] = u'40001'
            self.retjson['contents'] = u"该用户不存在"
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))



