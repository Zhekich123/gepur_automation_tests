from imports import *


def search_filter(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    report_path = ("/Users/zhekich/PycharmProjects/gepur_tests/gepur_automation_testing/gepur_automation_tests/test_filter_material_plus_tag.zip")

    page.hover(".styles_accordion__1nYPJ")   # open sidebar menu
    categories = page.locator("//a[@class='styles_panel-item__2qFev']").all()      # list of categories
    clothes = categories[1]   # odezhda sub menu
    clothes.click()

    sub_category = page.locator("//a[@class='styles_list_item__2msD6']").all()   # list of sub categories
    shirts = sub_category[8]  # shirts section
    shirts.click()
    page.wait_for_timeout(1000)

    tags = page.locator("//a[@class='styles_tag-item__2cwSh']").all()
    cotton_tag = tags[1]     # choose tag
    cotton_tag.click()
    page.wait_for_timeout(2000)

    page.click("//div[@class='styles_more-filters__1bNkD']")  # All filters button
    page.wait_for_timeout(500)

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


    context.tracing.stop(path=report_path)


def test_search_product_and_filter():
    with sync_playwright() as playwright:
        search_filter(playwright)