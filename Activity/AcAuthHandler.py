# coding=utf-8
import random
'''
@author:黄鑫晨
@introduction:返回活动创建权限
每次管理员手动申请后获得认证码
服务器返回验证码，交给活动发布方
活动发布后
'''

class AcAuthHandler(object):
    '''
        生成随机的字符串
    '''

    def get_auth(self):
        seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sa = []
        for i in range(32):
            sa.append(random.choice(seed))
        salt = ''.join(sa)
        print salt
        return salt

auth_handler = AcAuthHandler()
auth_handler.get_auth()