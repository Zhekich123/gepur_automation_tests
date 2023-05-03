from imports import *


def search_filter(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/en")

    page.hover(".styles_accordion__1nYPJ")  # open sidebar menu

    page.click("a[href^='/en/catalog/odezhda']")      # odezhda sub menu

    overalls = page.locator("a[href^='/en/catalog/kombinezony']")
    page.wait_for_timeout(1000)

    # page.click("//div[@class='promo-banner__close']")  # close banner

    if overalls.is_visible():
        overalls.click()
    else:
        page.goto("https://gepur.com/en/catalog/kombinezony")

    page.click("//div[@class='styles_s-filter__3N8-7']")  # sorting filter

    sorting_filters = page.locator("//li[@class='styles_item__1Gxg6']").all()  # from expensive to the cheapest filter
    expensive_to_cheapest = sorting_filters[0]
    expensive_to_cheapest .click()
    page.wait_for_timeout(1000)

    page.locator("//div[@class='catalog-origin__catalog-wrapper']/div").all()    # catalog

    prices = page.locator("//div[@class='styles_prices__7vcJI']").all()    # checking prices
    prev_price_value = None

    for i, price in enumerate(prices[:14]):
        price_value = int(''.join(filter(str.isdigit, price.inner_text())))
        if prev_price_value is not None:
            if price_value <= prev_price_value:
                print(f"\nPrice {price.inner_text()} at index {i} is less than or equal to previous price")
            else:
                print(f"\nERROR\nPrice {price.inner_text()} at index {i} is greater than previous price")

        prev_price_value = price_value



    context.tracing.stop(path=global_report_path)

def test_search_product_and_filter():
    with sync_playwright() as playwright:
        search_filter(playwright)