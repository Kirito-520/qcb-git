#姓名：麦文辉
#时间： 14:15

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1.打开网站
"""
xpath:
1、绝对路径：/html/body/div/div/div[1]/a/b   --根节点，顺序性，继承关系  --失效
== 面试不说，工作不用
2、相对路径：只靠自己的特征定位   // 开头 -- 加上我关心节点的标签名
==标签名+属性 =//标签名[@属性名=属性值]
//input[@id="username"]  --xpath表达方式

2、层级定位:
//标签名[@属性值]//标签名[@属性名=届性值]
-//div[@class="login-logo"]//b

3、文本属性定位://b[text()=“柠檬ERP"]

4、包含属性值://标签名[contains(@属性名/text(),属性值]
---//input[contains(@class,"username")]

"""


def open_url():
    global driver

    # 初始化Firefox浏览器 建立会话
    driver = webdriver.Firefox()

    # 打开网站
    driver.get('http://erp.lemfix.com/login.html')
    driver.implicitly_wait(10) # 隐式等待

    # 窗口最大化
    driver.maximize_window()

    # 向前一页
    driver.forward()

    # 向后一页
    driver.back()

    # 刷新
    driver.refresh()

    # 退出
    # driver.quit() # 关闭会话

    # 关闭当前窗口，不会退出会话
    # driver.close()

    # 对页面进行操作
    # 1.点击
    # 2.传值

    # 找到username id
    # driver.find_element(by=By.ID, value='username').send_keys('test123')
    driver.find_element(by=By.XPATH, value='//input[@id="username"]').send_keys('test123')

    # 找到元素后获取文本 赋值
    page_text = driver.find_element(by=By.XPATH, value='//div[@class="login-logo"]//b').text
    if page_text == '柠檬ERP':
        print('这个页面的标题为：{}'.format(page_text))
    else:
        print('这个条件测试用例不通过')
    # 找到password id
    driver.find_element(by=By.ID, value='password').send_keys('123456')
    # 点击登录
    driver.find_element(by=By.ID, value='btnSubmit').click()

    # 获取用户名
    login_user = driver.find_element(by=By.XPATH, value='//P[text()="测试用户"]').text
    if login_user == '测试用户':
        print('这个登录用户是：{}'.format(login_user))
    else:
        pass

    # 点击零售出库
    driver.find_element(by=By.XPATH, value='//span[text()="零售出库"]').click()

    # 1、识别是否有子页面的方式: 页面层级路径里出现iframe:就需要去切换iframe才可以进行元素的定位。
    # 2、怎么去切换:
    # 1）找到这个iframe元素，切换

    # 1、通过ID来切换
    P_id = driver.find_element(by=By.XPATH, value='//div[text()="零售出库"]/..').get_attribute('id')
    print(P_id + '-frame')
    # driver.switch_to.frame(P_id + '-frame')

    # 2.通过xpath定位切换
    driver.switch_to.frame(driver.find_element(by=By.XPATH, value='//iframe[@id="{}"]'.format(P_id + '-frame')))

    time.sleep(3)
    input_id = driver.find_element(by=By.XPATH, value='//input[@id="searchNumber"]')
    input_id.send_keys('9844')
    driver.find_element(by=By.ID, value='searchBtn').click()


if __name__ == '__main__':
    open_url()