#-*- coding:utf-8 -*-

'''
@黄鑫晨
@2016.10.30
用户形象展示
'''
class Upresentation(BaseHandler): #关于用户的一系列活动
    retjson = {'code': '400', 'contents': 'none'}
    def get(self):
        u_phone= self.get_argument('id')
        retdata = []