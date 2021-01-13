from base.web_base import WebBase
import page


class PageMpArticles(WebBase):
    # 1、点击创建榜单管理
    def page_click_rank_manage(self):
        self.base_click(page.mp_content_manage)

    # 2、点击创建榜单
    def page_click_rank_list(self):
        self.base_click(page.mp_content)

    # 2、点击创建榜单
    def page_click_add_rank(self):
        self.base_click(page.mp_click_add_rank)

    # 3、输入 名称
    def page_input_title(self):
        self.page_input_title()

    # 4、输入 标签
    def page_input_label(self):
        pass

    # 5、选择城市
    def page_click_city(self):
        pass

    # 6、输入排序
    def page_input_sort(self):
        pass

    # 7、上传榜单图
    def page_click_cover(self):
        pass

    # 8、上榜商家名称
    def page_input_merchants_title(self):
        pass

    # 9、店铺亮点
    def page_input_merchants_spot(self):
        pass

    # 10、店铺荣誉
    def page_input_merchants_honor(self):
        pass

    # 11、店铺宣传图
    def page_input_merchants_figure(self):
        pass

    # 12、点击保存按钮
    def page_click_sumbim(self):
        pass

    # 12、获取保存成功提示
    def page_get_info(self):
        pass

    # 13、组合发布榜单业务方法
    def page_mp_rank(self):
        pass
