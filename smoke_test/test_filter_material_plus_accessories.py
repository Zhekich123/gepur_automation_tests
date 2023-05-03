from imports import *


def search_filter(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    page.hover(".styles_accordion__1nYPJ")    # open sidebar menu
    page.wait_for_timeout(1000)
    page.click("a[href^='/uk/catalog/aksessuary']")
    show_all_accessories = page.locator("a[href^='/uk/catalog/aksessuary']").nth(1)
    show_all_accessories.click()

    # page.click("//div[@class='promo-banner__close']")   # close banner
    
    page.click("//div[@class='styles_more-filters__1bNkD']")  # All filters button
    page.wait_for_timeout(500)

    filters = page.locator("//div[@class='clearfix styles_filter-select__3qjY5']").all()  # list of filters
    material = filters[4]
    material.click()
    page.wait_for_timeout(500)

    page.click("a[href^='/uk/catalog/aksessuary?filters=materials:bizhuternyj-splav']") # filter

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


    context.tracing.stop(path=global_report_path)


def test_search_product_and_filter():
    with sync_playwright() as playwright:
        search_filter(playwright)