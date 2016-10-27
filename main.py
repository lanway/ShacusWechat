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
from Appointment.WAPselect import WAPselect
from Appointment.WAPcomment import APcommentHandler
from Appointment.WAPlistmodel import WAPListmodel
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
<<<<<<< HEAD
from Userinfo.UserAclist import UserAclist
from Userinfo.UserAplist import UserAplist
=======
from Userinfo.WUserhomepager import UHandler
>>>>>>> 34796e2edb20543b356acfa29f4f49f17f76d3b3
from Wechatserver.Wver import Wver

from Activity.WAcListAsk import AskActivity
from Activity.WAcregist import WAcregist
from Activity.WAcquitregist import WAquitcregist
from  Activity.AcInfo import AcInfoHandler

from Wechatserver.WBasic import WBasic
from Wechatserver.WgetSign import WgetSign
from Appointment.WAPCreatHandler import WAPCreatHandler
from Appointment.WAPListphoto import WAPListphoto
from Activity.WAcseeregist import WAcseeregist
from Appointment.WAPdetail import WAPdetail
from Appointment.WAPregist import WAPregist
from Appointment.WAPregistcancel import WAPregistcancel
from Appointment.WAPselectlist import WAPselectlist
#define("port", default=80, help="run on the given port", type=int)


from RegistandLogin.WRegisterHandler import WRegisterHandler
from RegistandLogin.WloginHandler import WLoginHandler
define("port", default=800, help="run on the given port", type=int)



class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(r"index.html")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            #(r"/bai")
            (r"/", IndexHandler),
            #(r"/",WBasic),
            (r"/weixin/activity/getauth", AcAuthHandler),
            (r"/weixin/activity/create", AcCreateHandler),
            (r"/weixin/activity/aclist",AskActivity),
            (r"/weixin/activity/regist",WAcregist),
            (r"/weixin/activity/quitregist",WAquitcregist),
            (r"/weixin/activity/detail",AcInfoHandler),
            (r"/weixin/activity/create", AcCreateHandler),
            (r"/weixin/getsign", WgetSign),
            (r"/weixin/appointment/ask", WAPCreatHandler),
            (r"/weixin/appointment/listphoto", WAPListphoto),
            (r"/weixin/appointment/listmodel",WAPListmodel),
            (r"/weixin/regist",WRegisterHandler),
            (r"/weixin/login", WLoginHandler),
            (r"/weixin/activity/registerlist",WAcseeregist),
            (r"/weixin/userpage/selfinfo", UHandler),
            (r"/weixin/appointment/info",WAPdetail),
            (r"/weixin/appointment/regist",WAPregist),
            (r"/weixin/appointment/registcancel",WAPregistcancel),
            (r"/weixin/appointment/selectlist",WAPselectlist),
<<<<<<< HEAD
            (r"/weixin/appointment/UserAclist", UserAclist),
            (r"/weixin/appointment/UserAplist", UserAplist),
=======
            (r"/weixin/appointment/select",WAPselect),
            (r"/weixin/appointment/comment",APcommentHandler)

>>>>>>> 34796e2edb20543b356acfa29f4f49f17f76d3b3
        ]

        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "template_path" : os.path.join(os.path.dirname(__file__), "static"),
        }  # 配置静态文件路径

        tornado.web.Application.__init__(self, handlers, **settings)


        self.db = scoped_session(sessionmaker(bind=engine,
                                              autocommit=False, autoflush=True,
                                              expire_on_commit=False))


if __name__ == "__main__":
    print "HI,I am in main "
    tornado.options.parse_command_line()
    Application().listen(options.port)

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()

