from imports import *

'''Выбор товара и добавление его в корзину'''

'''
    Given user is on the main page 
    When user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Аксесуари" button
    And user can click "Окуляри" button
    And user can click product 
    And user can click "Купити в 1 клік" button
    And user can see field with "phone field" 
    And user can input phone number into phone field
    And user can click "Купити в 1 клік"
    Then user can see the message "Access icon"  '''

def shopping_cart(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    phone = ("+380738983498")

    # page.click("//div[@class='modal-subscribe-close-button']")
    page.hover(".styles_accordion__1nYPJ")   #open sidebar memu
    page.click("a[href^='/uk/catalog/aksessuary']")
    page.click("a[href^='/uk/catalog/ochki']")

    # page.click("//div[@class='promo-banner__close']")  # close banner

    page.click("//div[@class='styles_product-slider__1D33N styles_expand-4__1CK38']")
    page.click("//button[@class='btn dark narrow skip-min-width v-space-md']")
    page.wait_for_timeout(1000)
    expect(page.locator("//div[@class='styles_checkbox__lsfu1']")).to_be_visible()
    page.click("//button[@class='btn light narrow']")
    page.wait_for_timeout(1000)

    field = page.locator("//input[@name='phone']")
    assert field.is_visible()
    assert field.input_value() == "+38 (___) __ __ ___"
    field.fill(phone)
    page.wait_for_timeout(500)
    # page.click("//button[@class='btn dark inside-input']")
    # expect(page.locator(".styles_icon__WEE7_")).to_be_visible()
    page.wait_for_timeout(1000)

    context.tracing.stop(path=global_report_path)

def test_choosing_product_and_add_to_cart():
    with sync_playwright() as playwright:
        shopping_cart(playwright)
