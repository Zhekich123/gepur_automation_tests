from imports import *


def search_filter(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    report_path = ("/Users/zhekich/PycharmProjects/gepur_tests/gepur_automation_testing/gepur_automation_tests/test_color_filters.zip")

    page.hover(".styles_accordion__1nYPJ")   # open sidebar menu
    categories = page.locator("//a[@class='styles_panel-item__2qFev']").all()  # list of categories
    clothes = categories[1]   # odezhda sub menu
    clothes.click()

    sub_category = page.locator("//a[@class='styles_list_item__2msD6']").all() # list of sub categories
    dresses = sub_category[2]  # dresses section
    dresses.click()
    page.wait_for_timeout(1000)


    page.evaluate('window.scrollBy(0, 200)')
    page.wait_for_timeout(1000)
    filters = page.locator("//div[@class='clearfix styles_filter-select__3qjY5']").all() # list of filters
    colors = filters[1]
    colors.click()
    page.wait_for_timeout(1000)


    list_of_colors = page.locator("//div[@class='styles_chip__1pd1y']").all()  # list of colors
    color_black = list_of_colors[19]
    color_black.click()
    page.wait_for_timeout(1000)

    show_buttons = page.locator("//button[@class='btn dark md']").all()  # accept button
    button = show_buttons[1]
    button.click()
    page.wait_for_timeout(1000)

    # page.click("//span[@class='text']")   # close pop-up menu

    items = page.locator("//div[@class='catalog-origin__catalog-wrapper']/div").all()
    random_element = random.choice(items)   # choose random product
    random_element.click()
    page.wait_for_timeout(2000)

    black_color = page.locator("//a[@class='styles_color-item__30d1- styles_chernyj__2HwwI']").all()
    choose_color = black_color[0]
    expect(choose_color).to_be_visible()

    context.tracing.stop(path=report_path)
def test_search_product_and_filter():
    with sync_playwright() as playwright:
        search_filter(playwright)