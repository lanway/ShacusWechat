# -*- coding: utf-8 -*-

'''
微信消息处理
'''
import json

from tornado.template import ParseError
from wechat_sdk.messages import TextMessage

from Wconf import Wconf
from BaseHandlerh import BaseHandler
from wechat_sdk import WechatBasic

class WBasic(BaseHandler):

    conf = Wconf.conf
    wechat = WechatBasic(conf=conf)

    def get(self):
        w_signature = self.get_argument('signature')
        w_timestamp = self.get_argument('timestamp')
        w_nonce = self.get_argument('nonce')
        w_echostr = self.get_argument('echostr')

        wechat = WechatBasic(conf=self.conf)
        if wechat.check_signature(w_signature, w_timestamp, w_nonce):
            print "成功了"
            self.write(json.dumps(int(w_echostr)))
        else:
            print "失败了"

    def post(self):
        body_text  = self.request.body
        try:
            self.wechat.parse_data(body_text)
        except ParseError:
            print 'Invalid Body Text'
        id = self.wechat.message.id  # 对应于 XML 中的 MsgId
        target = self.wechat.message.target  # 对应于 XML 中的 ToUserName
        source = self.wechat.message.source  # 对应于 XML 中的 FromUserName
        time = self.wechat.message.time  # 对应于 XML 中的 CreateTime
        type = self.wechat.message.type  # 对应于 XML 中的 MsgType
        raw = self.wechat.message.raw  # 原始 XML 文本，方便进行其他分析
        xml = ''
        if isinstance(self.wechat.message,TextMessage):
            content = self.wechat.message.content
            if content == '活动':
                xml = self.wechat.response_news([
                    {
                        'title': u'第一条新闻标题',
                        'description': u'第一条新闻描述，这条新闻没有预览图',
                        'url': u'http://www.google.com.hk/',
                    }
                ])

        self.write(xml)
