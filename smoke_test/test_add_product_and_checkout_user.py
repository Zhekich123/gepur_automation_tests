from imports import *

'''     
    And user can see that product into a cart
    And user can click "Оформити замовлення" button
    And user can see checkout menu
    And user can click "Нова Пошта - відділення" option
    And user can see "Дані отримувача та відділення" fields
    And user can input name
    And user can input phone number
    And user can input email
    And user can choose a city
    And user can choose department of post
    And user can click "Зберегти" button
    And user can see that delivery data is saved
    And user can click "Оплата карткою - онлайн"
    And user can see that checkbox is selected
    And user can see final block with product and price
    And user can click "Оформити замовлення" button
    And user can see purchase form
    And user can click button "back" in browser
    Then user can see the bill '''

def add_product_and_checkout(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://gepur.com/uk")
    page.hover(".styles_accordion__1nYPJ")
    page.get_by_role("link", name="Одяг", exact=True).click()
    page.get_by_role("link", name="Дивитися все").first.click()

   
def test_add_product_and_checkout_user():
    with sync_playwright() as playwright:
        add_product_and_checkout(playwright)