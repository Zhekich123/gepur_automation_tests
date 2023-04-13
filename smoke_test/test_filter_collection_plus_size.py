from imports import *


def search_filter(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    report_path = ("/Users/zhekich/PycharmProjects/gepur_tests/gepur_automation_testing/gepur_automation_tests/test_filter_collection_plus_size.zip")

    page.hover(".styles_accordion__1nYPJ")   # open sidebar menu
    categories = page.locator("//a[@class='styles_panel-item__2qFev']").all()      # list of categories
    clothes = categories[1]   # odezhda sub menu
    clothes.click()

    sub_category = page.locator("//a[@class='styles_list_item__2msD6']").all()   # list of sub categories
    see_all = sub_category[0]  # see all button
    see_all.click()
    page.wait_for_timeout(1000)

    page.click("//span[@class='text']")

    page.evaluate('window.scrollBy(0, 200)')
    page.wait_for_timeout(1000)
    filters = page.locator("//div[@class='clearfix styles_filter-select__3qjY5']").all()  # list of filters
    size_filter = filters[0]
    size_filter.click()
    page.wait_for_timeout(1000)


    sizes = page.locator("//div[@class='styles_chip__1pd1y styles_uppercase__3TPaN']").all()
    size_xs = sizes[15]     # sizes choosing
    size_xs.click()
    size_xs.click()

    show_buttons = page.locator("//button[@class='btn dark md']").all()  # accept button
    button = show_buttons[0]
    button.click()


    page.click("//div[@class='styles_more-filters__1bNkD']")  # All filters button
    page.wait_for_timeout(500)

    page.wait_for_timeout(1000)
    filters = page.locator("//div[@class='styles_filter-title__VyNld']").all()  # list of filters
    collection = filters[7]
    collection.click()
    page.wait_for_timeout(1000)

    collection_list = page.locator("//div[@class='styles_chip__1pd1y']").all()   # independent sub_filter
    independent = collection_list[150]
    independent.click()
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
    page.wait_for_timeout(4000)

    context.tracing.stop(path=report_path)


def test_search_product_and_filter():
    with sync_playwright() as playwright:
        search_filter(playwright)