# -*- coding: utf-8 -*-
'''
刷新微信access_token
'''
import ssl


from Wconf import Wconf
conf = Wconf.conf
def GetActoken():
    ssl._create_default_https_context = ssl._create_unverified_context
    conf.grant_access_token()
    conf.grant_jsapi_ticket()

GetActoken()