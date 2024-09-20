import time

from playwright.sync_api import Page, expect


def test_first_playwright_open_browser(page: Page):
    page.goto("https://duckduckgo.com/")
    print(page.url)

    page.locator("id=searchbox_input").fill("hello")
    page.locator("//button[@aria-label='Search']").click()

    expect(page.locator("id=search_form_input")).to_have_value("hello")
    # assert "hello" == page.input_value("id=search_form_input") #this is second approach to test

    page.locator("//h2/a/span").nth(4).wait_for()

    items = page.locator("//h2/a/span").all_text_contents()
    expect(page).to_have_title("hello at DuckDuckGo")
    assert len(items) > 0, "item is not null"
    # time.sleep(20)
