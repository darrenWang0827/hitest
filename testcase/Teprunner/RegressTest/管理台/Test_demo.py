from playwright.sync_api import sync_playwright

if __name__ == "__main__":
    with sync_playwright() as p:
        browser_type = p.chromium
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.baidu.com/")
        page.screenshot(path=f'demo-{browser_type.name}.png')
        browser.close()
