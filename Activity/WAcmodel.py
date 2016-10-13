# coding=utf-8
from Database.tables import UserImage, Image,WActivity, WAcImage
from FileHandler.Upload import AuthKeyHandler
from Database.models import get_db
'''
@author:王佳镭
'''
class ACmodelHandler:
    @classmethod
    def ac_Model_simply(clas,activity,retdata):
        '''得到简单活动模型
        :return:  retjson
        '''

        #get user_headimg
        user_headimages = get_db().query(UserImage).filter(UserImage.UIuid == activity.WACsponsorid ).all()
        userimg=[]
        for user_headimage in user_headimages:
            exist = get_db().query(Image).filter(Image.IMid == user_headimage.UIimid,Image.IMvalid == 1).all()
            if exist:
                userimg = user_headimage
                break;

        auth = AuthKeyHandler()
        #get activityimg
        aclurl = get_db().query(WAcImage).filter(WAcImage.WACIacid == activity.WACid).all()
        acurl = []
        for item in aclurl:
            Acurl = auth.download_url(item.WACIurl)
            acurl.append(Acurl)
        ac_simply_info = dict(
        WACid=activity.WACid,
        WACtitle=activity.WACtitle,
        WACstartT=activity.WACstartT.strftime('%Y-%m-%d %H:%M:%S'),
        WACprice = activity.WACprice,
        WACjoinT = activity.WACjoinT.strftime('%Y-%m-%d %H:%M:%S'),
        WACregistN = activity.WACregistN,
        Wacstatus = activity.WACstatus,
        WACimgurl= acurl,
        WUserimg = auth.download_url(userimg.UIurl)
        )
        return ac_simply_info
