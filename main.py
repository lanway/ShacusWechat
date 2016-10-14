# -*- coding: utf-8 -*-
'''
@author: 黄鑫晨
'''
#!/usr/bin/env python
import os

import tornado.httpserver
import  tornado.ioloop
import  tornado.options
import tornado.web
from sqlalchemy.orm import scoped_session, sessionmaker
from tornado.options import define, options


from Activity.AcAuthHandler import AcAuthHandler
from Database.models import engine
from Activity.AcCreateHandler import AcCreateHandler


from Activity.WAcListAsk import AskActivity
from Activity.WAcregist import WAcregist
from Activity.WAcquitregist import WAquitcregist

from  Activity.AcInfo import AcInfoHandler

# from ImageCallback import ImageCallback
# from RegisterHandler import RegisterHandler
# from Settings import PaswChange
# from Userinfo.UserFavoriteHandler import UserFavorite
# from Userinfo.UserIndent import UserIndent
# from Userinfo.UserInfo import UserInfo
# from Userinfo.UserLike import FindUlike
# from Userinfo.Userhomepager import Userhomepager
# from loginHandler import LoginHandler
from Wechatserver.Wver import Wver

from Activity.WAcListAsk import AskActivity
from Activity.WAcregist import WAcregist
from Activity.WAcquitregist import WAquitcregist
from  Activity.AcInfo import AcInfoHandler

from Wechatserver.WBasic import WBasic
from Wechatserver.WgetSign import WgetSign
from Appointment.WAPCreatHandler import WAPCreatHandler
from Appointment.WAPList import WAPList
from Activity.WAcseeregist import WAcseeregist
#define("port", default=80, help="run on the given port", type=int)


from RegistandLogin.WRegisterHandler import WRegisterHandler
from RegistandLogin.WloginHandler import WLoginHandler
define("port", default=800, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(r"static/index.html")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [

             (r"/", IndexHandler),
             (r"/weixin/activity/getauth", AcAuthHandler),
             (r"/weixin/activity/create", AcCreateHandler),
             (r"/weixin/activity/aclist",AskActivity),
             (r"/weixin/activity/regist",WAcregist),
             (r"/weixin/activity/quitregist",WAquitcregist),
             (r"/weixin/activity/detail",AcInfoHandler),
             (r"/weixin/activity/create", AcCreateHandler),
             (r"/weixin/getsign", WgetSign),
             (r"/weixin/appointment/ask", WAPCreatHandler),
             (r"/weixin/appointment/list", WAPList),
             (r"/weixin/regist",WRegisterHandler),
             (r"/weixin/login", WLoginHandler),
             (r"/weixin/activity/registerlist",WAcseeregist)
        ]
        tornado.web.Application.__init__(self, handlers, static_path, template_path, debug=True)

        self.db = scoped_session(sessionmaker(bind=engine,
                                              autocommit=False, autoflush=True,
                                              expire_on_commit=False))

# session负责执行内存中的对象和数据库表之间的同步工作 Session类有很多参数,使用sessionmaker是为了简化这个过程
#template_path = os.path.join(os.path.dirname(__file__), "temploop")
static_path = os.path.join(os.path.dirname(__file__), "static")
template_path = os.path.join(os.path.dirname(__file__), "static")


if __name__ == "__main__":
    print "HI,I am in main "
    tornado.options.parse_command_line()
    Application().listen(options.port)

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()

