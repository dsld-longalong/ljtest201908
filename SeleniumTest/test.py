#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #模拟鼠标
from selenium.webdriver.support.ui import WebDriverWait
import time
from userdata import get_webinfo,get_userinfo
from log_module import Loginfo 


def get_ele_times(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def openBrower():#打开浏览器
    webdriver_handle = webdriver.Firefox()
    return webdriver_handle

def openUrl(handle,url):#打开网址
    handle.get(url)
    #handle.maximize_window()

def findElement(d, arg):#arg must be a dict
    if 'text_id' in arg:
        ele_login=get_ele_times(d,10,lambda d: d.find_element_by_link_text(arg['text_id']))
        ele_login.click()
    useEle=d.find_element_by_css_selector(arg['userid'])
    pwdEle=d.find_element_by_css_selector(arg['pwdid'])
    loginEle=d.find_element_by_id(arg['loginid'])
    return useEle,pwdEle,loginEle

def sendVals(eletuple,arg):
    '''
    ele tuple
    account:uname,pwd
    '''
    listkey = ['uname','pwd']
    i = 0
    for key in listkey:
        eletuple[i].send_keys('')
        eletuple[i].clear()
        eletuple[i].send_keys(arg[key])
        i+=1
        
    eletuple[2].click()

def checkResult(d,err_id,arg,log):
    result = False #代表检查结果错误 ---------------------------1
    time.sleep(2)
    try:
        err=d.find_element_by_css_selector(err_id)
        print("Account And Pwd Error!")
        
        e=err.text #把抓取的值赋值给变量e，以变量e的格式储存
        #str(err.text)str无法直接读取
        msg='uname=%s pwd=%s:error:%s\n'%(arg['uname'],arg['pwd'],e)
        print(str(e)) #解析e以string的方式，显示当时错误提示的文字
        log.log_write(msg)
    except:
        msg='uname=%s pwd=%s:pass\n'%(arg['uname'],arg['pwd'])
        log.log_write(msg)
        print("Account And Pwd Rignt!")
        result = True #-----------------------------------------2
    return result#----------------------------------------------3

def logout(d,ele_dict):#---------新增接口-----------------------5
    #d.find_element_by_class_name(ele_dict['usermenu']).click()#注销所属目录现网页已经没有了
    d.find_element_by_css_selector(ele_dict['logout']).click()#注销
    
def login_test(ele_dict,user_list):
    d=openBrower()#打开浏览器
    log=Loginfo()
    openUrl(d,ele_dict['url'])#打开网址
    #5
    
    ele_tuple=findElement(d, ele_dict)
    for arg in user_list:
        sendVals(ele_tuple,arg)
        #arg是账户和密码
        result = checkResult(d,ele_dict['errorid'],arg,log)#---4
        if result:#如果返回True也就是登陆成功则回复现场1.注销logout2.重新登陆login
            logout(d,ele_dict)
            ele_tuple=findElement(d,ele_dict)#重新login
    log.log_close()

if __name__ == '__main__':
    
    ele_dict= get_webinfo(r'C:/Users/Yang Xiu Yu/Desktop/webinfo.txt')
    user_list=get_userinfo(r'C:\Users\Yang Xiu Yu\Desktop\userinfo.txt')

    login_test(ele_dict,user_list)

from selenium import webdriver

from time import sleep

browser = webdriver.Chrome()

browser.get('http://www.baidu.com')

  #等待网页加载

browser.find_element_by_css_selector('#u1 .lb').click()  #通过class来获取DOM元素

#browser.find_element_by_css_selector("#u1 > a[name='tj_login']").click() #通过标签来获取取DOM元素

sleep(2)  #等待网页加载

browser.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()

browser.find_element_by_id('TANGRAM__PSP_10__userName').send_keys('***')

browser.find_element_by_id('TANGRAM__PSP_10__password').send_keys('***')

browser.find_element_by_id('TANGRAM__PSP_10__submit').click()
