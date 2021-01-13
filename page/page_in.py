from page.page_mp_login import PageMpLogin
# from page.page_mp_rank import PageMpRank


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    # # 获取PageMpRank对象
    # def page_get_PageMpRank(self):
    #     return PageMpRank(self.driver)
