from imports import *

''' Given user is on the page
    When user click "Account button" on home page
    And user can see "Телефон або email" field
    And user can input correct email in "Телефон або email" field
    And user can see "Введіть пароль" field
    And user can input correct password in "Введіть пароль" field
    And user can click "Вхід" button
    And user can see that he successfully login  
    And user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Аксесуари" button
    And user can click "Окуляри" button
    And user can click product 
    And user click "В кошик" button  
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
    And user can click on block with commentaries 
    And user can see commentaries field
    And user can leave a comment
    And user can click "Зберегти" button
    And user can see that comment text is saved
    And user can see final block with product and price
    And user can click "Оформити замовлення" button
    And user can click button "back" in browser
    Then user can see the bill '''

def add_product_and_checkout(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    context.clear_cookies()
    page.goto("https://gepur.com/uk")

    page.click("//a[@class='service_button account_icon']")
    expect(page.locator("//input[@name='phoneOrEmail']")).to_be_visible()
    page.fill("//input[@name='phoneOrEmail']", "test14364accounnt@gmail.com")
    page.click("//span[text()='Далі']")
    expect(page.locator("//input[@type='password']")).to_be_visible()
    page.fill("//input[@type='password']", "Test1234567890")
    page.click("//span[text()='Вхід']")
    page.wait_for_timeout(1000)
    page.hover("//a[@class='service_button account_icon']")
    locator = page.locator("//div[@class='drop_down']")
    expect(locator).to_be_visible()
    page.wait_for_timeout(1000)

    page.hover(".styles_accordion__1nYPJ")
    expect(page.locator("//div[@class='styles_panel_list__28Ix6']")).to_be_visible()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="Аксесуари", exact=True).click()
    page.get_by_role("link", name="Окуляри", exact=True).click()
    page.wait_for_timeout(1000)
    page.click("//span[text()='Сонцезахисні окуляри']")

    page.click("//span[text()='В кошик']")
    page.wait_for_timeout(1000)
    expect(page.locator("//div[@class='styles_checkbox__lsfu1']")).to_be_visible()
    page.click("//a[text()='Оформити замовлення']")
    expect(page.locator("// div[ @class ='styles_header-checkout__1L94N']")).to_be_visible()
    page.wait_for_timeout(3000)

    # page.click("//div[text()='Нова Пошта - відділення']")
    page.click("//div[text()='Інша адреса']")
    page.wait_for_timeout(1000)
    # expect(page.locator("//div[text()='Дані отримувача та відділення']")).to_be_visible()
    expect(page.locator("//div[text()='Змінити адресу']")).to_be_visible()
    page.click("//span[text()='Додати адресу']")


    page.fill("//input[@name='name']", "Тестове Замовлення")
    page.fill("//input[@name='phone']", "+380738983498")
    mista = page.locator("//div[@class='styles_input-wrap__1AQ5I']").all()
    misto = mista[1]
    misto.click()
    page.click("//div[text()='Львів']")


    viddilenya_all = page.locator("//div[@class='styles_input-wrap__1AQ5I']").all()
    viddilenya = viddilenya_all[2]
    viddilenya.click()
    page.wait_for_timeout(1000)

    list_of_departaments = page.locator("//div[@class='styles_list-block__z4mCg v-space']").all()
    departament = list_of_departaments[0]
    departament.click()
    # page.click("//div[text()='Відділення №1: вул. Городоцька, 359']")
    # page.click("//div[text()='Відділення №21 (до 30 кг на одне місце): просп. Олександрівський, 21']")
    page.click("//span[text()='Зберегти']")
    page.click("//span[text()='Підтвердити']")
    page.wait_for_timeout(1000)

    expect(page.locator("//div[text()='Дані отримувача']")).to_be_visible()
    page.click("//div[text()='Оплата карткою - онлайн']")
    page.click("//div[text()='Коментар до замовлення']")
    expect(page.locator("//div[text()='Додати коментар']")).to_be_visible()
    page.wait_for_timeout(1000)
    page.fill("//textarea[@maxlength='1000']", "Тестове замовлення, IT відділ, не передзванюйте будь ласка")
    page.wait_for_timeout(1000)
    page.click("//span[text()='Зберегти']")
    page.wait_for_timeout(1000)
    expect(page.locator("//div[text()='Тестове замовлення, IT відділ, не передзванюйте будь ласка']")).to_be_visible()
    expect(page.locator("//div[@class='styles_wrap__1lgHX styles_selected__GWoli']")).to_be_visible()
    expect(page.locator("//div[@class='styles_summary-content__3IqCA']")).to_be_visible()
    page.click("//span[text()='Оформити замовлення']")
    page.wait_for_timeout(2000)
    # expect(page.locator("//form[@class='payment-form']")).to_be_visible()
    page.go_back()
    expect(page.locator("//div[@class='styles_title__14p_x']")).to_be_visible()


def test_add_product_and_checkout_user():
    with sync_playwright() as playwright:
        add_product_and_checkout(playwright)
