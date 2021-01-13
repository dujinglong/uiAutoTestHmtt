from page.page_in import PageIn
import pytest

from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 1、获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2、通过统一入口类获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageMpLogin()

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize("username,code,expect", read_yaml("mp_login.yaml"))
    # 没有参数化直接使用值
    # def test_mp_login(self, username="18321252140", code="123456", expect="文章列表")
    def test_mp_login(self, username, code, expect):
        # 调用登录业务方法
        self.mp.page_mp_login(username, code)
        try:
            # 断言
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            log.error("断言出错，错误信息：{}".format(e))
            print("错误原因：", e)
            self.mp.base_get_img()
            # 抛出异常
            raise


