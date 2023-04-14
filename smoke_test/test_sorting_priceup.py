from imports import *


def search_filter(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    report_path = ("/Users/zhekich/PycharmProjects/gepur_tests/gepur_automation_testing/gepur_automation_tests/test_sorting_priceup.zip")

    page.hover(".styles_accordion__1nYPJ")  # open sidebar menu
    categories = page.locator("//a[@class='styles_panel-item__2qFev']").all()  # list of categories
    novelties = categories[0]  # novelties

    if novelties.is_visible():
        novelties.click()
    else:
        page.goto("https://gepur.com/uk/catalog/novinki")

    page.click("//div[@class='styles_s-filter__3N8-7']")    # sorting filter

    sorting_filters = page.locator("//li[@class='styles_item__1Gxg6']").all()  # from cheapest to expensive filter
    cheapest_to_expensive = sorting_filters[1]
    cheapest_to_expensive.click()
    page.wait_for_timeout(1000)

    page.locator("//div[@class='catalog-origin__catalog-wrapper']/div").all()    # catalog

    prices = page.locator("//div[@class='styles_prices__7vcJI']").all()
    prev_price_value = None

    for i, price in enumerate(prices[:16]):
        price_value = int(''.join(filter(str.isdigit, price.inner_text())))
        if prev_price_value is not None:
            if price_value >= prev_price_value:
                print(f"\nPrice {price.inner_text()} at index {i} is greater than or equal to previous price")
            else:
                print(f"\nERROR\nPrice {price.inner_text()} at index {i} is less than previous price")

        prev_price_value = price_value

    context.tracing.stop(path=report_path)

def test_search_product_and_filter():
    with sync_playwright() as playwright:
        search_filter(playwright)