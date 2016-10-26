# -*- coding: utf-8 -*-
'''
刷新微信access_token
'''
<<<<<<< HEAD
import urllib
=======
import ssl

>>>>>>> 7a712d7481e323bac1f3169205a3f6fcdad58335

import requests
import ssl
from Wconf import Wconf
conf = Wconf.conf
def GetActoken():
<<<<<<< HEAD
    context = ssl._create_unverified_context()
    urllib.urlopen("https://api.weixin.qq.com/cgi-bin/token", context=context)
    urllib.urlopen("https://api.weixin.qq.com/cgi-bin/ticket/getticket", context=context)
    requests.get('https://api.weixin.qq.com/cgi-bin/token', verify=True)
    requests.get('https://api.weixin.qq.com/cgi-bin/ticket/getticket', verify=True)
    # This restores the same behavior as before.

=======
    ssl._create_default_https_context = ssl._create_unverified_context
>>>>>>> 7a712d7481e323bac1f3169205a3f6fcdad58335
    conf.grant_access_token()
    conf.grant_jsapi_ticket()

GetActoken()