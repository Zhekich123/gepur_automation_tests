from imports import *


def search_filter(playwright: Playwright, test_name: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    page.hover(".styles_accordion__1nYPJ")   # open sidebar menu
    page.click("a[href^='/uk/catalog/odezhda']")
    show_all = page.locator("a[href^='/uk/catalog/odezhda']").nth(1)
    show_all.click()
    page.wait_for_timeout(1000)

    # page.click("//div[@class='promo-banner__close']")  # close banner
    # page.click("//span[@class='text']")

    page.evaluate('window.scrollBy(0, 200)')
    page.wait_for_timeout(1000)
    filters = page.locator("//div[@class='clearfix styles_filter-select__3qjY5']").all()  # list of filters
    size_filter = filters[0]
    size_filter.click()
    page.wait_for_timeout(1000)


    size_xs = page.locator("a[href^='/uk/catalog/odezhda?filters=size:xs']").all()
    size = size_xs[1]
    expect(size).to_be_visible()
    size.click()
    # sizes = page.locator("//div[@class='styles_chip__1pd1y styles_uppercase__3TPaN']").all()
    # size_xs = sizes[15]     # sizes choosing
    # size_xs.click()
    # size_xs.click()

    show_buttons = page.locator("//button[@class='btn dark md']").all()  # accept button
    button = show_buttons[0]
    button.click()


    page.click("//div[@class='styles_more-filters__1bNkD']")  # All filters button

    page.wait_for_timeout(1000)
    filters = page.locator("//div[@class='styles_filter-title__VyNld']").all()  # list of filters
    collection = filters[7]
    collection.click()
    page.wait_for_timeout(1000)

    page.click("a[href^='/uk/catalog/odezhda?filters=collection:nezalezhna']")
    page.wait_for_timeout(1000)

    show_buttons = page.locator("//button[@class='btn dark md']").all()  # accept button
    button = show_buttons[7]
    button.click()
    page.wait_for_timeout(1000)

    items = page.locator("//div[@class='catalog-origin__catalog-wrapper']/div").all()
    random_element = random.choice(items)  # choose random product
    random_element.click()
    page.wait_for_timeout(2000)

    buttons_size = page.locator("//div[@class='styles_size__eFSdz styles_selected__2In_k']").all()
    button_xs = buttons_size[0]     # size xs button
    expect(button_xs).to_be_visible()
    expect(button_xs).to_be_enabled()
    page.wait_for_timeout(1000)

    global_report_path = get_report_path(test_name)
    context.tracing.stop(path=global_report_path)


def test_search_product_and_filter():
    with sync_playwright() as playwright:
        test_name = "test_filter_collection_plus_size"
        get_report_path(test_name)
        search_filter(playwright, test_name)
