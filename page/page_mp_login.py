from base.base import Base
import page
from time import sleep
from tools.get_log import GetLog
log = GetLog.get_logger()


class PageMpLogin(Base):
    # 输入用户手机号
    def page_input_username(self, username):
        # 调用父类中输入方法
        self.base_input(page.mp_username, username)

    # 输入验证码
    def page_input_code(self, code):
        # 调用父类中输入方法
        self.base_input(page.mp_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        # 调用父类中点击方法
        self.base_click(page.mp_login_btn)
        sleep(3)

    # 获取昵称封装 ——>测试脚本层断言使用
    def page_get_nickname(self):
        # 调用父类中获取文本方法
        return self.base_get_text(page.mp_nickname)

    # 组合业务方法 ->测试脚本层调用
    def page_mp_login(self, username, code):
        log.info("正在调用运营后台登录业务方法，用户名：{}密码：{}".format(username, code))
        """提示：调用相同页面操作步骤，跨页面暂时不考虑"""
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()

    # 组合业务方法 ->排行榜依赖使用
    def page_mp_login_bank(self, username="18321252140", code="123456"):
        log.info("正在调用运营后台登录业务方法，用户名：{}密码：{}".format(username, code))
        """提示：调用相同页面操作步骤，跨页面暂时不考虑"""
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()

