"""以下为运营后台管理url"""
# 运营后台url
url_mp = "http://test.www.aixiangdao.cn/admin/dist/index.html#/login"
# h5的url地址
url_mis = "https://h5.aixingdao.top/develop"

from selenium.webdriver.common.by import By
"""以下数据为运营后台系统配置数据"""
# 用户名

mp_username = (By.CSS_SELECTOR, "[placeholder='用户名']")
# 验证码
mp_code = (By.CSS_SELECTOR, "[placeholder='密码']")
# 登录按钮
mp_login_btn = (By.CSS_SELECTOR, ".el-button--primary")
# 断言添加文章页面
mp_nickname = (By.CSS_SELECTOR, "[class='no-redirect']")
# 点击发布文章
mp_content_manage = By.XPATH, "el-menu-item is-active"
# 选择文章管理
mp_click_rank = By.XPATH, "//*[@id=\"app\"]/div/div[1]/div[1]/div/ul/div/li[2]/div/span"
# 选择创建榜单
mp_click_add_rank = By.XPATH, "//*[text()='+创建']"
# 选择创建榜单
mp_add_rank_title = By.XPATH, "//*[@id=\"root\"]/div/section/section/main/div/div[2]/div/div[2]/div/div[1]/div/text()"
# iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 文章内容 定位body,勿定位到P标题
mp_content = By.CSS_SELECTOR, "#tinymce"
# 封面
mp_cove = By.XPATH, "//*[text()='自动']"

