# -*- coding: utf-8 -*-
'''
刷新微信access_token
'''
import requests

from Wconf import Wconf
conf = Wconf.conf
def GetActoken():
    requests.get('https://api.weixin.qq.com/cgi-bin/token', verify=True)
    requests.get('https://api.weixin.qq.com/cgi-bin/ticket/getticket', verify=True)
    conf.grant_access_token()
    conf.grant_jsapi_ticket()

GetActoken()