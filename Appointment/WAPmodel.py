# -*-coding:utf-8 -*-
'''
@author :兰威
@type：微信的约拍模型
@datatime：2016.10.10
'''
from Database.models import get_db
from FileHandler.Upload import AuthKeyHandler
class WAPmodel(object):

    def wap_model_simply_one(self,wap,picurl):
        '''

        Args:
            wap: 约拍的一个实例
            picurl: 约拍图片的地址（第一张）

        Returns: wap简单模型

        '''
        auth = AuthKeyHandler()
        ret_ap = dict(
            title=wap.WAPtitle,
            content=wap.WAPcontent[0:12],
            picurl=auth.download_url(picurl),
            id=wap.WAPid,
            detailurl='www.baidu.com'  #当前传的是一个假的值

        )
        return ret_ap

    def wap_model_simply_more(self,waps,picurls):
        '''

        Args:
            waps: 约拍实例的元组
            picurls: 约拍图片地址的元组

        Returns:

        '''
        retedate = []
        for wap,picurl in zip(waps,picurls):
            data = self.wap_model_simply_one(wap,picurl)
            retedate.append(data)
        return retedate

