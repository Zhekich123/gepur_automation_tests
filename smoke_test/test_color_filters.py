from imports import *


def search_filter(playwright: Playwright, test_name: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    page.hover(".styles_accordion__1nYPJ")   # open sidebar menu
    page.click("a[href^='/uk/catalog/odezhda']")
    page.click("a[href^='/uk/catalog/platya']")
    page.wait_for_timeout(1000)

    # page.click("//div[@class='promo-banner__close']")  # close banner
    # page.click("//span[@class='text']")  # close pop-up menu

    page.evaluate('window.scrollBy(0, 200)')
    page.wait_for_timeout(1000)
    filters = page.locator("//div[@class='clearfix styles_filter-select__3qjY5']").all() # list of filters
    colors = filters[1]
    colors.click()
    page.wait_for_timeout(1000)

    page.click("a[href^='/uk/catalog/platya?filters=color:chernyj']")
    page.wait_for_timeout(1000)

    show_buttons = page.locator("//button[@class='btn dark md']").all()  # accept button
    button = show_buttons[1]
    button.click()
    page.wait_for_timeout(1000)

    items = page.locator("//div[@class='catalog-origin__catalog-wrapper']/div").all()
    random_element = random.choice(items)   # choose random product
    random_element.click()
    page.wait_for_timeout(2000)

    black_color = page.locator("//a[@class='styles_color-item__30d1- styles_chernyj__2HwwI']").all()
    choose_color = black_color[0]
    expect(choose_color).to_be_visible()

    global_report_path = get_report_path(test_name)
    context.tracing.stop(path=global_report_path)
def test_search_product_and_filter():
    with sync_playwright() as playwright:
        test_name = "test_color_filters"
        get_report_path(test_name)
        search_filter(playwright, test_name)
