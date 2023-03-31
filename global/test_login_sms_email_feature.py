from imports import *

'''Логин в хедере через email'''

''' Given user is on the page
    When user click "Account button" on home page
    And user can see "Телефон або email" field
    And user can input correct email in "Телефон або email" field
    And user can see "Введіть пароль" field
    And user can input correct password in "Введіть пароль" field
    And user can click "Вхід" button
    Then user can see that he successfully login '''

def header_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://next.gepur.org/uk")

    page.click("//div[@class='modal-subscribe-close-button']")
    page.click("//a[@class='service_button account_icon']")
    page.fill("//input[@name='phoneOrEmail']", "test14366accounnt@gmail.com")
    page.click("//span[text()='Далі']")
    page.fill("//input[@type='password']", "Test1234567890")
    page.click("//span[text()='Вхід']")
    page.wait_for_timeout(1000)

    page.hover("//a[@class='service_button account_icon']")
    locator = page.locator("//div[@class='drop_down']")
    expect(locator).to_be_visible()

    page.click("//span[@class='logout-btn']")




    '''Логин в хедере через SMS'''

    ''' Given user is on the page
        When user click "Account button" on home page
        And user can see "Телефон або email" field
        And user can input correct value in "Телефон або email" field
        And user can see "Введіть код" field
        And user can input correct value in "Введіть код" field
        And user can click "Підтвердити" button
        Then user can see that he successfully login '''

    page.wait_for_timeout(1500)
    page.click("//a[@class='service_button account_icon']")
    page.fill("//input[@name='phoneOrEmail']", "380632206190")
    page.click("//span[text()='Далі']")
    get_sms_data()
    page.fill("//input[@name='codeSMS']", get_code())
    page.click("//span[text()='Підтвердити']")
    page.wait_for_timeout(1500)

    page.hover("//a[@class='service_button account_icon']")
    locator = page.locator("//div[@class='drop_down']")
    expect(locator).to_be_visible()

    page.click("//span[@class='logout-btn']")


    context.close()
    browser.close()

def test_login_in_header_email_and_sms():
    with sync_playwright() as playwright:
        header_login(playwright)


'''Логин в сайдбаре через email'''

''' Given user is on the page
    When user point mouse on the "Sidebar" menu in home page
    And user can click "Особистий кабінет" button
    And user can see "Телефон або email" field
    And user can input correct email in "Телефон або email" field
    And user can see "Введіть пароль" field
    And user can input correct password in "Введіть пароль" field
    And user can click "Вхід" button
    Then user can see that he successfully login '''

def sidebar_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://next.gepur.org/uk")

    page.click("//div[@class='modal-subscribe-close-button']")
    page.locator(".styles_accordion__1nYPJ").click()
    page.click("//span[text()='Особистий кабінет']")
    page.fill("//input[@name='phoneOrEmail']", "test14366accounnt@gmail.com")
    page.click("//span[text()='Далі']")
    page.fill("//input[@type='password']", "Test1234567890")
    page.click("//span[text()='Вхід']")
    page.wait_for_timeout(1500)

    page.hover("//a[@class='service_button account_icon']")
    locator = page.locator("//div[@class='drop_down']")
    expect(locator).to_be_visible()

    page.locator(".styles_accordion__1nYPJ").click()
    page.click("//span[text()='Особистий кабінет']")
    page.click("//span[text()='Вихід']")



    '''Логин в сайдбаре через SMS'''

    ''' Given user is on the page
        When user point mouse on the "Sidebar" menu in home page
        And user can click "Особистий кабінет" button
        And user can see "Телефон або email" field
        And user can input correct value in "Телефон або email" field
        And user can see "Введіть код" field
        And user can input correct value in "Введіть код" field
        And user can click "Підтвердити" button
        Then user can see that he successfully login '''


    page.wait_for_timeout(1500)
    page.locator(".styles_accordion__1nYPJ").click()
    page.click("//span[text()='Особистий кабінет']")
    page.fill("//input[@name='phoneOrEmail']", "380673527974")
    page.click("//span[text()='Далі']")
    get_sms_data()
    page.fill("//input[@name='codeSMS']", get_code())
    page.click("//span[text()='Підтвердити']")
    page.wait_for_timeout(1500)

    page.hover("//a[@class='service_button account_icon']")
    locator = page.locator("//div[@class='drop_down']")
    expect(locator).to_be_visible()

    page.locator(".styles_accordion__1nYPJ").click()
    page.click("//span[text()='Особистий кабінет']")
    page.click("//span[text()='Вихід']")
    page.wait_for_timeout(1500)

    context.close()
    browser.close()

def test_login_in_sidebar_email_and_sms():
    with sync_playwright() as playwright:
        sidebar_login(playwright)