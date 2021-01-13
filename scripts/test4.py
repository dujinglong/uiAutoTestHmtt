"""
    需求：
        1、使用百度搜索python案例
        2、分别运行chrom和firefox中运行
"""

# 1、导包
# from selenium import webdriver
# from time import sleep
# import threading
# # 2、封装百度
# def get_baidu(driver):
#     # 打开url
#     driver.get("http：//www.baidu,com")
#     # 输入python
#     driver.find_elemnt_by_id("kw").send_keys("python")
#     # 点击搜索按钮
#     driver.find_elemnt_by_id("su").click()
#     # 暂停及关闭
#     sleep(3)
#     driver.quit()
#
# # 3.封装driver
# def get_driver(browser):
#     # 定义空变量
#     cap = None
#     # 判断浏览器类型
#     if browser == "chrome":
#         cap = webdriver.DesiredCapabilities.CHROME.copy()
#     elif browser == "firefox":
#         cap = webdriver.DesiredCapabilities.FIREFOX.copy()
#     # 修改默认平台名称
#     cap['paltform'] = 'WINDOWS'
#     # 返回driver
#     return webdriver.Remote("http://127.0.0.1:4444/wd/hub", cap)
# # 4.遍历多线程
# # 定义浏览器列表
# browserName =['chrome', 'firefox']
# # 遍历浏览器列表
# for browser in browserName:
#     # 获取driver
#     driver = get_driver(browser)
#     # 实例化线程及启动
#     threading.Thread(target=get_baidu, args=(driver,)).start()