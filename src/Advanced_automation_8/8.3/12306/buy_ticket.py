# -*- coding: utf-8 -*-
"""
@author: liuyw
"""
from splinter.browser import Browser
from time import sleep
import traceback
import time, sys

class huoche(object):
    '''docstring for huoche'''
    driver_name=''
    executable_path=''
    #用户名密码
    username = u"xxx@qq.com"
    passwd = u"xxxx"

    starts = u"%u4E0A%u6D77%2CSHH"
    ends = u"%u592A%u539F%2CTYV"
    # ʱ���ʽ2018-01-19
    dtime = u"2018-01-19"
   
    order = 0
    
    users = [u"xxx",u"xxx"]
    ##ϯλ
    xb = u"������"
    pz=u"����Ʊ"
    """��ַ"""
    ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    login_url = "https://kyfw.12306.cn/otn/login/init"
    initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
    buy="https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    login_url='https://kyfw.12306.cn/otn/login/init'
    
    def __init__(self):
        self.driver_name='chrome'
        self.executable_path='/usr/local/bin/chromedriver'
    
    def login(self):
        self.driver.visit(self.login_url)
        self.driver.fill("loginUserDTO.user_name", self.username)
        # sleep(1)
        self.driver.fill("userDTO.password", self.passwd)
        print u"�ȴ���֤�룬��������..."
        while True:
            if self.driver.url != self.initmy_url:
                sleep(1)
            else:
                break
    
    def start(self):
        self.driver=Browser(driver_name=self.driver_name,executable_path=self.executable_path)
        self.driver.driver.set_window_size(1400, 1000)
        self.login()
        # sleep(1)
        self.driver.visit(self.ticket_url)
        try:
            print u"��Ʊҳ�濪ʼ..."
            # sleep(1)
            # ���ز�ѯ��Ϣ
            self.driver.cookies.add({"_jc_save_fromStation": self.starts})
            self.driver.cookies.add({"_jc_save_toStation": self.ends})
            self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
            self.driver.reload()
            count=0
            if self.order!=0:
                while self.driver.url==self.ticket_url:
                    self.driver.find_by_text(u"��ѯ").click()
                    count += 1
                    print u"ѭ�������ѯ... �� %s ��" % count
                    # sleep(1)
                    try:
                        self.driver.find_by_text(u"Ԥ��")[self.order - 1].click()
                    except Exception as e:
                        print e
                        print u"��û��ʼԤ��"
                        continue
            else:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text(u"��ѯ").click()
                    count += 1
                    print u"ѭ�������ѯ... �� %s ��" % count
                    # sleep(0.8)
                    try:
                        for i in self.driver.find_by_text(u"Ԥ��"):
                            i.click()
                            sleep(1)
                    except Exception as e:
                        print e
                        print u"��û��ʼԤ�� %s" %count
                        continue
                        print u"��ʼԤ��..."
                        # sleep(3)
                        # self.driver.reload()
                        sleep(1)
                        print u'��ʼѡ���û�...'
                        for user in self.users:
                            self.driver.find_by_text(user).last.click()
                            print u"�ύ����..."
                            sleep(1)
                            # self.driver.find_by_text(self.pz).click()
                            # self.driver.find_by_id('').select(self.pz)
                            # # sleep(1)
                            # self.driver.find_by_text(self.xb).click()
                            # sleep(1)
                            self.driver.find_by_id('submitOrder_id').click()
                            # print u"��ʼѡ��..."
                            # self.driver.find_by_id('1D').last.click()
                            # self.driver.find_by_id('1F').last.click()
                            sleep(1.5)
                            print u"ȷ��ѡ��..."
                            self.driver.find_by_id('qr_submit_id').click()
        except Exception as e:
            print e

if __name__ == '__main__':
    huoche=huoche()
    huoche.start()