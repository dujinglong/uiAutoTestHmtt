from time import sleep
from base.base import Base
from selenium.webdriver.common.by import By


class WebBase(Base):
    """以下均为web项目专属方法"""
    def web_base_click_elemnt(self, class_text, click_text):
        # 1、点击复选框
        loc = By.XPATH, "//div[contains(@class,'el-input__inner')]".format(class_text)
        self.base_click(loc)
        # 2、暂时
        sleep(1)
        # 3、点击包含显示文本的元素
        loc = By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/button".format(click_text)
        self.base_click(loc)
