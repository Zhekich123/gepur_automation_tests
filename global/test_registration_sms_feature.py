from playwright.sync_api import expect

from imports import *

'''Регистрация в хедере через SMS'''

''' Given user is on the page
    When user click "Account button" on home page
    And user can click "Реєстрація" button
    And user can see "П.І.Б" field
    And user can input correct value in "П.І.Б" field
    And user can see "Телефон" field
    And user can input correct value in "Телефон" field
    And user can see "Email" field
    And user can input correct value in "Email" field
    And user can see "Введіть пароль" field
    And user can input correct value in "Введіть пароль" field
    And user can click "Зареєструватися" button
    And user can see "Введіть код із СМС" field
    And user can input code into "Введіть код із СМС" field
    And user can click "Підтвердити" button
    Then user can see that he successfully login '''

def header_registration(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://next.gepur.org/uk")

    page.click("//div[@class='modal-subscribe-close-button']")
    page.click("//a[@class='service_button account_icon']")
    page.click("//span[text()='Реєстрація']")
    page.fill("//input[@name='fio']", user_random)
    page.fill("//input[@name='phone']", phone_number)
    page.fill("//input[@name='email']", random_email + "@gmail.com")
    page.fill("//input[@name='password']", "Test1234567890")
    page.click("//span[text()='Зареєструватися']")
    page.wait_for_timeout(500)
    get_sms_data()
    page.fill("//input[@name='codeSMS']", get_code())
    page.click("//span[text()='Підтвердити']")
    page.wait_for_timeout(500)

    page.hover("//a[@class='service_button account_icon']")
    locator = page.locator("//div[@class='drop_down']")
    expect(locator).to_be_visible()

    page.wait_for_timeout(500)
    page.click("//span[@class='logout-btn']")



def test_header_registration_with_sms():
    with sync_playwright() as playwright:
        header_registration(playwright)



'''Регистрация в сайдбаре через SMS'''

''' Given user is on the page
    When user point mouse on sidebar menu in home page
    And user can click "Особистий кабінет" button
    And user can click "Реєстрація" button
    And user can see "П.І.Б" field
    And user can input correct value in "П.І.Б" field
    And user can see "Телефон" field
    And user can input correct value in "Телефон" field
    And user can see "Email" field
    And user can input correct value in "Email" field
    And user can see "Введіть пароль" field
    And user can input correct value in "Введіть пароль" field
    And user can click "Зареєструватися" button
    And user can see "Введіть код із СМС" field
    And user can input code into "Введіть код із СМС" field
    And user can click "Підтвердити" button
    Then user can see that he successfully login '''

def sidebar_registration(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://next.gepur.org/uk")

    page.click("//div[@class='modal-subscribe-close-button']")
    page.hover(".styles_accordion__1nYPJ")
    page.click("//span[text()='Особистий кабінет']")
    page.click("//span[text()='Реєстрація']")
    page.fill("//input[@name='fio']", user_random)
    page.fill("//input[@name='phone']", phone_number2)
    page.fill("//input[@name='email']", random_email2 + "@gmail.com")
    page.fill("//input[@name='password']", "Test1234567890")
    page.click("//span[text()='Зареєструватися']")
    page.wait_for_timeout(500)
    get_sms_data()
    page.fill("//input[@name='codeSMS']", get_code())
    page.click("//span[text()='Підтвердити']")

    page.hover("//a[@class='service_button account_icon']")
    locator = page.locator("//div[@class='drop_down']")
    expect(locator).to_be_visible()

    page.hover(".styles_accordion__1nYPJ")
    page.wait_for_timeout(1000)
    page.click("//span[text()='Особистий кабінет']")
    page.wait_for_timeout(500)
    page.click("//span[text()='Вихід']")

    context.close()
    browser.close()


def test_sidebar_registration_with_sms():
    with sync_playwright() as playwright:
        sidebar_registration(playwright)

