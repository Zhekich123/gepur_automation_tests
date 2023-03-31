from imports import *

'''Выбор товара и добавление его в корзину'''

'''
    Given user is on the main page 
    When user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Одяг" button
    And user can click "Дивитися все" button
    And user can click any size to "Додати до кошыка" any product 
    And user can add this product into a cart
    And user can click "Кошик" button
    And user can see that size is the same as user choose
    And user can see that coast is the same as in product
    Then user can see that product successfully added into a cart
                                                                   '''

def shopping_cart(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    # page.click("//div[@class='modal-subscribe-close-button']")
    page.locator(".styles_accordion__1nYPJ").click()
    page.click("//span[text()='Одяг']")
    page.wait_for_selector("//span[text()='Дивитися все']")
    page.locator("//span[text()='Дивитися все']").nth(1).click()
    items = page.locator_all("//div[@class='styles_catalog-item-block__1qjsB styles_width-view--1__1R44V']")
    page.wait_for_timeout(2000)
    random_element = random.choices(items)
    random_element.click()
    page.wait_for_timeout(4000)



def test_choosing_product_and_add_to_cart():
    with sync_playwright() as playwright:
        shopping_cart(playwright)

