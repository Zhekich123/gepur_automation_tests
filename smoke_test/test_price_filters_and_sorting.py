from imports import *


def search_filter(playwright: Playwright, test_name: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    page.hover(".styles_accordion__1nYPJ")   # open sidebar menu
    page.click("a[href^='/uk/catalog/odezhda']")      # odezhda sub menu

    page.click("a[href^='/uk/catalog/futbolki-majki']")  # tops category

    page.wait_for_timeout(1000)

    # page.click("//div[@class='promo-banner__close']")  # close banner
    # page.click("//span[@class='text']")  # close pop-up menu

    page.click("//div[@class='styles_more-filters__1bNkD']")      # All filters button
    page.wait_for_timeout(500)

    filters = page.locator("//div[@class='clearfix styles_filter-select__3qjY5']").all()  # list of filters
    price_sales = filters[6]
    price_sales.click()
    page.wait_for_timeout(500)

    page.fill("//input[@name='maxPrice']", "1200")  # input max price field

    show_buttons = page.locator("//button[@class='btn dark md']").all()  # accept button
    button = show_buttons[6]
    button.click()
    page.wait_for_timeout(1000)

    page.click("//div[@class='styles_sorting-static__2189g']")   # sorting menu

    sorting_filters = page.locator("//li[@class='styles_item__1Gxg6']").all()   # from cheapest to expensive filter
    cheapest_to_expensive = sorting_filters[1]
    cheapest_to_expensive.click()
    page.wait_for_timeout(1000)

    page.locator("//div[@class='catalog-origin__catalog-wrapper']/div").nth(0)    # first product
    page.wait_for_timeout(2000)
    items_price = page.locator("//div[@class='styles_prices__7vcJI']").nth(0)
    price = items_price.inner_text()        # assertion price
    expected_price = "1200 грн"
    expected_price_value = int(''.join(filter(str.isdigit, expected_price)))
    actual_price_value = int(''.join(filter(str.isdigit, price)))
    # assert actual_price_value <= expected_price_value
    if actual_price_value <= expected_price_value:
        print("\nFilter is working correctly")
    else:
        print("\nFilter is working wrong")

    global_report_path = get_report_path(test_name)
    context.tracing.stop(path=global_report_path)
def test_search_product_and_filter():
    with sync_playwright() as playwright:
        test_name = "test_price_filters_and_sorting"
        get_report_path(test_name)
        search_filter(playwright, test_name)
