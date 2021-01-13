'''
    目标：selenium Grid的使用
    需求：
    1、打开chrome浏览器
    2、打开百度并搜索python关键字
    3、暂停3秒 关闭浏览器
'''
# 导包
# from selenium import webdriver
# from time import sleep
# # 获取driver
# # driver = webdriver.Chrome()
# # 重点 driver获取
# cap = {
#     "browserName": "chrome",
#     "platform": "WINDOWS"
# }
# driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", cap)
# # 打开百度
# driver.get("http://www.baidu.com")
# # 输入关键字
# driver.find_element_by_id("kw").send_keys("python")
# # 点击搜索按钮
# driver.find_element_by_id("su").click()
# # 暂停3秒 关闭浏览器
# sleep(3)
# driver.quit()
