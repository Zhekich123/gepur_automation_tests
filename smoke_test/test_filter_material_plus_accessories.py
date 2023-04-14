from imports import *


def search_filter(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    report_path = ("/Users/zhekich/PycharmProjects/gepur_tests/gepur_automation_testing/gepur_automation_tests/test_filter_material_plus_accessories.zip")

    page.hover(".styles_accordion__1nYPJ")    # open sidebar menu
    page.wait_for_timeout(1000)
    categories = page.locator("//a[@class='styles_panel-item__2qFev']").all()   # open categories
    accessories = categories[7]
    accessories.click()

    sub_category = page.locator("//a[@class='styles_list_item__2msD6']").all()   # open sub category
    show_all = sub_category[23]
    show_all.click()

    page.click("//div[@class='styles_more-filters__1bNkD']")  # All filters button
    page.wait_for_timeout(500)

    filters = page.locator("//div[@class='clearfix styles_filter-select__3qjY5']").all()  # list of filters
    material = filters[4]
    material.click()
    page.wait_for_timeout(500)

    sub_filters = page.locator("//div[@class='styles_chip__1pd1y']").all()   # choosing filter
    jewelry_alloy = sub_filters[1]
    jewelry_alloy.click()

    show_buttons = page.locator("//button[@class='btn dark md']").all()  # accept button
    button = show_buttons[4]
    button.click()
    page.wait_for_timeout(1000)

    items = page.locator("//div[@class='catalog-origin__catalog-wrapper']/div").all()
    random_element = random.choice(items)  # choose random product
    random_element.click()
    page.wait_for_timeout(2000)

    texts = page.locator("//a[@class='styles_link__2ZW6P styles_material__2qsha v-space-sm']").all()
    first_text = texts[0]
    text_value = first_text.inner_text()

    uk_text = "Біжутерний Сплав"
    en_text = "Jewelry Alloy"
    ru_text = "Бижутерный Сплав"

    if uk_text in text_value:
        print("\nHere's text: Біжутерний Сплав")
    elif en_text in text_value:
        print("\nHere's text: Jewelry Alloy")
    else:
        print("\nHere's text: Бижутерный Сплав")


    context.tracing.stop(path=report_path)


def test_search_product_and_filter():
    with sync_playwright() as playwright:
        search_filter(playwright)