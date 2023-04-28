from imports import *


def search_filter(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    report_path = ("/Users/zhekich/PycharmProjects/gepur_tests/gepur_automation_testing/gepur_automation_tests/reports/test_search.zip")

    page.click("//div[@class='styles_search__3RqsL']")
    search_modal = page.locator("//div[@class='styles_search-header__4cYGA styles_show__24tgV']")
    expect(search_modal).to_be_visible()
    search = page.locator("//input[@type='search']")
    search.fill("@№%#$!")
    page.click("//button[@type='submit']")
    not_found_message = page.locator("//div[@class='styles_not-found__1z_PQ']")

    expect(not_found_message).to_be_visible()

    text_in_message = page.locator("//div[@class='styles_not-found__1z_PQ']").inner_text()

    if "@№%" in text_in_message:
        print("\nMessage is right")
    else:
        print("\nMessage is wrong or not find")




    context.tracing.stop(path=report_path)


def test_search_product_and_filter():
    with sync_playwright() as playwright:
        search_filter(playwright)