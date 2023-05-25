from imports import *

''' Given user is on the page
    When user click "Account button" on home page
    And user can see "phone або email" field
    And user can input correct email in "phone або email" field
    And user can see "enter password" field
    And user can input correct password in "Enter password" field
    And user can click "Enter" button
    And user can see that he successfully login  
    And user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Accessories" button
    And user can click "Glasses" button
    And user can click product 
    And user click "A Cart" button  
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

def add_product_and_checkout(playwright: Playwright, test_name: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    phone = ("+380933346641")
    email = ("bolsunovska.daria@gmail.com")
    password = ("92e3579aSun")

    page.click("//a[@class='service_button account_icon']")
    expect(page.locator("//input[@name='phoneOrEmail']")).to_be_visible()
    page.fill("//input[@name='phoneOrEmail']", email)
    page.click("//button[@class='btn dark narrow skip-min-width  v-space-bt']")
    expect(page.locator("//input[@type='password']")).to_be_visible()
    page.fill("//input[@type='password']", password)
    page.click("//button[@class='btn dark narrow skip-min-width ']")
    page.wait_for_timeout(1000)
    page.hover("//a[@class='service_button account_icon']")
    locator = page.locator("//div[@class='drop_down']")
    expect(locator).to_be_visible()
    page.wait_for_timeout(1000)


    page.hover(".styles_accordion__1nYPJ")
    page.wait_for_timeout(1000)
    page.hover(".styles_accordion__1nYPJ")  # open sidebar memu
    page.click("a[href^='/uk/catalog/aksessuary']")  # choose glasses category
    page.click("a[href^='/uk/catalog/ochki']")

    # page.click("//div[@class='promo-banner__close']")  # close banner
    # page.click("//span[@class='text']")

    page.click("//div[@class='styles_product-slider__1D33N styles_expand-4__1CK38']")
    page.click("//button[@class='btn dark narrow skip-min-width v-space-md']")
    page.wait_for_timeout(1000)
    expect(page.locator("//div[@class='styles_info__3Q3n6']")).to_be_visible()
    page.click("//div[@class='button-link-wrapper full']")
    expect(page.locator("// div[ @class ='styles_header-checkout__1L94N']")).to_be_visible()
    page.wait_for_timeout(3000)

    types_of_posts = page.locator("//div[@class='styles_cap__l28lf']").all()
    new_post = types_of_posts[0]
    new_post.click()
    page.click("//div[@class='styles_button__2j2NM styles_change__eWg1L v-space']")
    expect(page.locator("//div[@class='styles_label__uUxAi']")).to_be_visible()
    page.click("//button[@class='btn light narrow skip-min-width skip-padding']")

    page.fill("//input[@name='name']", "Тестове Замовлення")
    page.fill("//input[@name='phone']", phone)
    cities_button = page.locator("//div[@class='styles_input-wrap__1AQ5I']").all()
    city_menu = cities_button[1]
    city_menu.click()
    cities_list = page.locator("//div[@class='styles_options-item__2vKps']").all()
    city = cities_list[1]
    city.click()

    departaments_button = page.locator("//div[@class='styles_input-wrap__1AQ5I']").all()
    departaments = departaments_button[2]
    departaments.click()
    page.wait_for_timeout(1000)

    departaments_list = page.locator("//div[@class='styles_options-item__2vKps']").all()
    departament = departaments_list[3]
    departament.click()

    page.click("//div[@class='styles_save__oBaAg']")
    page.click("//button[@class='btn narrow skip-min-width skip-padding v-space']")
    page.wait_for_timeout(1000)

    expect(page.locator("//div[@class='styles_address__19pO3 v-space']")).to_be_visible()

    payment_menu = page.locator("//div[@class='styles_section-title__1PWpd }']").nth(1)
    expect(payment_menu).to_be_visible()
    online_payment = page.locator("//div[@class='styles_wrap__1lgHX styles_selected__GWoli']")
    online_payment.click()

    page.click("//div[@class='styles_cap__1cn_6']")
    page.click("//div[@class='styles_wrap__1lgHX styles_selected__GWoli']")
    page.click("//div[@class='styles_label__2RfoE']")
    expect(page.locator("//div[@class='styles_label__uUxAi']")).to_be_visible()
    page.wait_for_timeout(1000)
    page.fill("//textarea[@maxlength='1000']", "Тестове замовлення, IT відділ, не передзвонюйте будь ласка")
    page.wait_for_timeout(1000)
    page.click("//button[@class='btn narrow skip-min-width skip-padding']")
    page.wait_for_timeout(1000)
    expect(page.locator("//div[@class='styles_comment__7_U0V']")).to_be_visible()
    expect(page.locator("//div[@class='styles_wrap__1lgHX styles_selected__GWoli']")).to_be_visible()
    expect(page.locator("//div[@class='styles_summary-content__3IqCA']")).to_be_visible()

    # page.click("//button[@class='btn dark narrow skip-min-width skip-padding v-space styles_primary-color__3fKw9']")
    # page.wait_for_timeout(2000)

    # payment_content_header = page.locator("//div[@class='payment-form-title']")
    # expect(payment_content_header).to_be_visible()

    # page.go_back()
    #
    # order_details = page.locator("//div[@class='styles_content__38zNh v-space-md']")
    # expect(order_details).to_be_visible()

    global_report_path = get_report_path(test_name)
    context.tracing.stop(path=global_report_path)
def test_add_product_and_checkout_user():
    with sync_playwright() as playwright:
        test_name = "test_add_product_and_checkout_user"
        get_report_path(test_name)
        add_product_and_checkout(playwright, test_name)
