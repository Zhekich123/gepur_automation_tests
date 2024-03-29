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
    search.fill("436")
    page.click("//button[@type='submit']")

    not_found_message = page.locator("//div[@class='styles_not-found__1z_PQ']")
    expect(not_found_message).to_be_visible()

    text_in_message = page.locator("//div[@class='styles_not-found__1z_PQ']").inner_text()

    if "436" in text_in_message:
        print("\nMessage is right")
    else:
        print("\nMessage is wrong or not find")

    global_report_path = get_report_path(test_name)
    context.tracing.stop(path=global_report_path)


def test_search_product_and_filter():
    with sync_playwright() as playwright:
        test_name = "test_search_input_part_of_vendor_code"
        get_report_path(test_name)
        search_filter(playwright, test_name)
