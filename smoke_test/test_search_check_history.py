from imports import *


def search_filter(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    page.click("//div[@class='styles_search__3RqsL']")
    search_modal = page.locator("//div[@class='styles_search-header__4cYGA styles_show__24tgV']")

    expect(search_modal).to_be_visible()
    search = page.locator("//input[@type='search']")

    search_input = "Платье"
    search.fill(search_input)
    page.click("//button[@type='submit']")

    page.click("//div[@class='styles_search__3RqsL']")
    search_history = page.locator("//div[@class='swiper-slide swiper-slide-active styles_query-item__12WPw']").inner_text()

    if search_history == "Платье":
        print("\nText is: 'Платье'")
    else:
        print("\nHistory is not visible or incorrect")

    page.wait_for_timeout(1000)




    context.tracing.stop(path=global_report_path)


def test_search_product_and_filter():
    with sync_playwright() as playwright:
        search_filter(playwright)