'''
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    page.locator("#kw").click()
    page.locator("#kw").fill("如何使用playwright")
    page.locator("#kw").press("Enter")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="playwright基本使用 - 简书").click()
    page1 = page1_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
'''
# 以上内容由playwright框架录制生成的脚本，可增加断言后转换成unittest格式的用例

import unittest
from util.Decorator import custom_skipUnless
from playwright.sync_api import Playwright, sync_playwright, expect

class Test_record_demo(unittest.TestCase):
    """
    测试用例类，类名可以按照 'Test_模块_功能_正向' 命名
    类中，只需要写测试用例，每个测试用例是一个方法，每个方法将前面写好的api resource 进行组合实现测试功能
    """

    @custom_skipUnless(["debug","regress"])
    def test_case_1(self):
        """
        【用例名称】：试用playwright测试web ui
        【预期结果】：略
        """
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://www.baidu.com/")
            page.locator("#kw").click()
            page.locator("#kw").fill("如何使用playwright")
            page.locator("#kw").press("Enter")
            with page.expect_popup() as page1_info:
                page.get_by_role("link", name="playwright基本使用 - 简书").click()
            page1 = page1_info.value

            # ---------------------
            context.close()
            browser.close()



if __name__ == "__main__":
    pass
