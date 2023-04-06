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
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")
    # page.click("//div[@class='modal-subscribe-close-button']")
    page.hover(".styles_accordion__1nYPJ")
    page.get_by_role("link", name="Аксесуари", exact=True).click()
    page.get_by_role("link", name="Окуляри", exact=True).click()
    page.wait_for_timeout(1000)
    page.click("//span[text()='Сонцезахисні окуляри']")

    page.click("//span[text()='Купити в 1 клік']")
    # buttons = page.locator("button").all()
    # third_button = buttons[3]
    # third_button.click()
    # page.wait_for_timeout(500)

    field = page.locator("input").all()
    first_field = field[2]
    assert first_field.is_visible()
    assert first_field.input_value() == "+38 (___) __ __ ___"
    first_field.fill("+380738983498")
    page.wait_for_timeout(500)

    buy_button = page.locator("//button[@type='submit']").all()
    four_button = buy_button[1]
    four_button.click()
    page.wait_for_timeout(1000)
    expect(page.locator(".styles_icon__WEE7_")).to_be_visible()
    page.wait_for_timeout(1000)

    # context.tracing.stop(path="/Users/zhekich/PycharmProjects/gepur_tests/gepur_automation_testing/gepur_automation_tests/trace.zip")


def test_choosing_product_and_add_to_cart():
    with sync_playwright() as playwright:
        shopping_cart(playwright)
