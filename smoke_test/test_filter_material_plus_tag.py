from imports import *


def search_filter(playwright: Playwright, test_name: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    page.hover(".styles_accordion__1nYPJ")   # open sidebar menu
    page.click("a[href^='/uk/catalog/odezhda']")
    page.click("a[href^='/uk/catalog/bluzy-rubashki']")

    page.wait_for_timeout(1000)

    # page.click("//div[@class='promo-banner__close']")  # close banner
    # page.click("//span[@class='text']")   # close pop-up menu

    page.click("a[href^='/uk/catalog/bluzy-rubashki?filters=materials:proshva']")   # tag proshva

    # page.wait_for_timeout(2000)

    page.click("//div[@class='styles_more-filters__1bNkD']")  # All filters button

    page.wait_for_timeout(1000)
    filters = page.locator("//div[@class='clearfix styles_filter-select__3qjY5']").all()   # list of filters
    material = filters[5]
    material.click()

    cotton_selected = page.locator("//div[@class='styles_chip__1pd1y styles_selected__3tBcb']")
    expect(cotton_selected).to_be_visible()         # check if cotton is selected
    page.wait_for_timeout(1000)

    buttons_reset = page.locator("//span[@class='button-icon-content']").all()   # button reset
    button_reset = buttons_reset[10]
    button_reset.click()
    page.wait_for_timeout(1000)

    all_button = page.locator("//a[@class='styles_tag-item__2cwSh styles_active__2PTuy']")
    expect(all_button).to_be_visible()

    global_report_path = get_report_path(test_name)
    context.tracing.stop(path=global_report_path)


def test_search_product_and_filter():
    with sync_playwright() as playwright:
        test_name = "test_filter_material_plus_tag"
        get_report_path(test_name)
        search_filter(playwright, test_name)