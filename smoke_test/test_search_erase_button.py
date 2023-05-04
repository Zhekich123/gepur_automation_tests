from imports import *


def search_filter(playwright: Playwright, test_name: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    page.click("//div[@class='styles_search__3RqsL']")
    search_modal = page.locator("//div[@class='styles_search-header__4cYGA styles_show__24tgV']")

    expect(search_modal).to_be_visible()
    search = page.locator("//input[@type='search']")
    search.fill("Джинсовий сарафан")

    search_text = page.locator("//input[@value='Джинсовий сарафан']")
    expect(search_text).to_be_visible()


    page.click("//span[@class='styles_cross__1wBF8']")  # erase button

    empty_field = search.inner_text()

    if "" in empty_field:
        print("\nErase button is work correct")
    else:
        print("\nErase button is  not working")

    global_report_path = get_report_path(test_name)
    context.tracing.stop(path=global_report_path)


def test_search_product_and_filter():
    with sync_playwright() as playwright:
        test_name = "test_search_erase_button"
        get_report_path(test_name)
        search_filter(playwright, test_name)