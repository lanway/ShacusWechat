# -*- coding: utf-8 -*-
'''
刷新微信access_token
'''
import urllib

import requests
import ssl
from Wconf import Wconf
conf = Wconf.conf
def GetActoken():
    context = ssl._create_unverified_context()
    urllib.urlopen("https://api.weixin.qq.com/cgi-bin/token", context=context)
    urllib.urlopen("https://api.weixin.qq.com/cgi-bin/ticket/getticket", context=context)
    requests.get('https://api.weixin.qq.com/cgi-bin/token', verify=True)
    requests.get('https://api.weixin.qq.com/cgi-bin/ticket/getticket', verify=True)
    # This restores the same behavior as before.

    conf.grant_access_token()
    conf.grant_jsapi_ticket()

GetActoken()