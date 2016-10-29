#-*- coding:utf-8 -*-

'''
@黄鑫晨
@2016.10.30
用户形象展示
'''
import json

from BaseHandlerh import BaseHandler
from Database.tables import User, Homepageimage
from FileHandler.Upload import AuthKeyHandler

class Upresentation(BaseHandler): # 返回用户形象展示的信息
    retjson = {'code': '400', 'contents': 'none', 'imgtokens':'','imgurls':'','alais':''}
    def get(self):
        utel = self.get_argument('utel')
        callback = self.get_argument("jsoncallback")
        try:
            user = self.db.query(User).filter(User.Utel == utel).one()
            auth_key_handler = AuthKeyHandler()
            uid = user.Uid
            ualais = user.Ualais
            if ualais:
                self.retjson['alais'] = ualais
            img_tokens = []
            img_urls = []
            try:
                u_homepage_imgs = self.db.query(Homepageimage).filter(Homepageimage.HPuser == uid).all()
                for each in u_homepage_imgs:
                    img_url = each.HPimgurl
                    img_tokens.append(auth_key_handler.download_url(img_url))
                    img_urls.append(img_url)
                self.retjson['imgtokens'] = img_tokens
                self.retjson['imgurls'] = img_urls
                self.retjson['code'] = u'200'
                self.retjson['contents'] = u'返回成功'
            except Exception, e:
                self.retjson['code'] = u'200'
                self.retjson['contents'] = u'返回成功'
        except Exception, e:
            print e
            self.retjson['code'] = '40001'
            self.retjson['contents'] = '该用户不存在'
        jsonp = "{jsfunc}({json});".format(jsfunc=callback, json=json.dumps(self.retjson, ensure_ascii=False, indent=2))
        self.write(jsonp)
