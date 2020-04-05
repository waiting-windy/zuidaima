import time
import datetime
from selenium import webdriver
import ins

username = "964879015@qq.com" #登录账号
password = "******"#登录密码
message = ins.getInstance()

driver = webdriver.Chrome() #模拟谷歌浏览器打开网站
driver.get("http://www.zuidaima.com/user/login.htm")

try:
    #输入用户名
    driver.find_element_by_id("account").send_keys(username)
    time.sleep(1)
    #输入密码
    driver.find_element_by_id("password").send_keys(password)
    time.sleep(1)
    #点击登录
    driver.find_element_by_id("login").click()
    time.sleep(1)

    driver.get("http://www.zuidaima.com/")

    #输入签到信息
    driver.find_element_by_id("mood_input").send_keys(message.strip())
    time.sleep(1)

    #完成签到
    driver.find_element_by_id("mood_publish").click()
    time.sleep(1)

    print("签到成功")


except:

    print("签到失败")

driver.quit()


    
