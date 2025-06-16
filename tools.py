from crewai.tools import BaseTool
from playwright.sync_api import sync_playwright
import time

class PlaywrightLoginTool(BaseTool):

    name: str = "playwright_login_tool"
    description: str = "A tool to perform login actions using Playwright."

    def _run(self, url: str, username: str, password: str) -> str:
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False, slow_mo=100)
                page = browser.new_page()
                page.goto(url)

                page.get_by_role('link', name='Log in').click()

                with page.expect_popup() as popup_info: 
                    page.get_by_role('button', name='Continue with Google').click()

                popup_page = popup_info.value

                popup_page.wait_for_load_state('domcontentloaded')
                time.sleep(2)

                popup_page.locator('#identifierId').fill(username)

                popup_page.get_by_role('button', name='Next').click()

                popup_page.wait_for_load_state('domcontentloaded')
                time.sleep(2)

                popup_page.get_by_label('Enter your password').fill(password)
                popup_page.get_by_role('button', name='Next').click()

                time.sleep(15)

                if page.locator("text='Welcome to Notion!'").first.is_visible():
                    browser.close()
                    return "Login successful."
                else:
                    browser.close()
                    return "Login failed. Check credentials or selectors."


        except Exception as e:
            return f"An error occurred during login: {e}"