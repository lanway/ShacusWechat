# -*- coding: utf-8 -*-
'''
@author: 黄鑫晨
'''
#!/usr/bin/env python
import tornado.httpserver
import  tornado.ioloop
import  tornado.options
import tornado.web
from sqlalchemy.orm import scoped_session, sessionmaker
from tornado.options import define, options

# from Activity.ACHandler import ActivityCreate, ActivityRegister
# from Activity.ACaskHandler import AskActivity
# from Activity.ACentryHandler import AskEntry
# from Appointment.APAskHandler import APaskHandler
# from Appointment.APCreateHandler import APcreateHandler
# from Appointment.APRegistHandler import APregistHandler
# from Appointment.Ranklist import Ranklist
# from Course.Chomepage import Chomepage
# from Course.CourseAsk import CourseAsk
# from Course.CourseLike import Courselike
# from Course.Coursefav import Coursefav
from Activity.AcAuthHandler import AcAuthHandler
from Database.models import engine
from Activity.AcCreateHandler import AcCreateHandler
# from ImageCallback import ImageCallback
# from RegisterHandler import RegisterHandler
# from Settings import PaswChange
# from Userinfo.UserFavoriteHandler import UserFavorite
# from Userinfo.UserIndent import UserIndent
# from Userinfo.UserInfo import UserInfo
# from Userinfo.UserLike import FindUlike
# from Userinfo.Userhomepager import Userhomepager
# from loginHandler import LoginHandler
#from Wechatserver.Wver import Wver
#from Wechatserver.WBasic import WBasic
#from Wechatserver.WgetSign import WgetSign
#from Appointment.WAPCreatHandler import WAPCreatHandler
#from Appointment.WAPList import WAPList
define("port", default=800, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [

          #   (r"/", WBasic),
             (r"/weixin/activity/getauth", AcAuthHandler),
             (r"/weixin/activity/create", AcCreateHandler)
             # (r"/weixin/getsign", WgetSign),
             # (r"/weixin/appointment/ask", WAPCreatHandler),
             # (r"/weixin/appointment/list", WAPList)
        ]
        tornado.web.Application.__init__(self, handlers)
        self.db = scoped_session(sessionmaker(bind=engine,
                                              autocommit=False, autoflush=True,
                                              expire_on_commit=False))

# session负责执行内存中的对象和数据库表之间的同步工作 Session类有很多参数,使用sessionmaker是为了简化这个过程
if __name__ == "__main__":
    print "HI,I am in main "
    tornado.options.parse_command_line()
    Application().listen(options.port)

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()

