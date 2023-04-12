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

def add_product_and_checkout(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://gepur.com/uk")

    page.click("//a[@class='service_button account_icon']")
    expect(page.locator("//input[@name='phoneOrEmail']")).to_be_visible()
    page.fill("//input[@name='phoneOrEmail']", "test14364accounnt@gmail.com")
    page.click("//button[@class='btn dark narrow skip-min-width  v-space-bt']")
    expect(page.locator("//input[@type='password']")).to_be_visible()
    page.fill("//input[@type='password']", "Test1234567890")
    page.click("//button[@class='btn dark narrow skip-min-width ']")
    page.wait_for_timeout(1000)
    page.hover("//a[@class='service_button account_icon']")
    locator = page.locator("//div[@class='drop_down']")
    expect(locator).to_be_visible()
    page.wait_for_timeout(1000)


    page.hover(".styles_accordion__1nYPJ")
    page.wait_for_timeout(1000)
    categories = page.locator("//a[@class='styles_panel-item__2qFev']").all()
    accessories = categories[7]
    accessories.click()
    sub_category = page.locator("//a[@class='styles_list_item__2msD6']").all()
    glasses = sub_category[26]
    glasses.click()
    page.wait_for_timeout(1000)
    page.click("//div[@class='styles_product-slider__1D33N styles_expand-4__1CK38']")
    page.click("//button[@class='btn dark narrow skip-min-width v-space-md']")
    page.wait_for_timeout(1000)
    expect(page.locator("//div[@class='styles_checkbox__lsfu1']")).to_be_visible()
    page.click("//div[@class='button-link-wrapper full']")
    expect(page.locator("// div[ @class ='styles_header-checkout__1L94N']")).to_be_visible()
    page.wait_for_timeout(4000)

    page.click("//span[@class='text']")

    types_of_posts = page.locator("//div[@class='styles_cap__l28lf']").all()
    new_post = types_of_posts[0]
    new_post.click()
    page.click("//div[@class='styles_button__2j2NM styles_change__eWg1L v-space']")
    expect(page.locator("//div[@class='styles_label__uUxAi']")).to_be_visible()
    page.click("//button[@class='btn light narrow skip-min-width skip-padding']")

    page.fill("//input[@name='name']", "Тестове Замовлення")
    page.fill("//input[@name='phone']", "+380738983498")
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
    ul_delivery_and_payment_section = page.locator("//ul[@class='styles_menu__2rwEx']").all()
    select_section = ul_delivery_and_payment_section[1]
    option = select_section.locator("li:nth-child(3)")
    option.click()

    page.click("//div[@class='styles_cap__1cn_6']")
    page.click("//div[@class='styles_wrap__1lgHX styles_selected__GWoli']")
    page.click("//div[@class='styles_label__2RfoE']")
    expect(page.locator("//div[@class='styles_label__uUxAi']")).to_be_visible()
    page.wait_for_timeout(1000)
    page.fill("//textarea[@maxlength='1000']", "Тестове замовлення, IT відділ, не передзванюйте будь ласка")
    page.wait_for_timeout(1000)
    # page.click("//button[@class='btn narrow skip-min-width skip-padding']")
    # page.wait_for_timeout(1000)
    # expect(page.locator("//div[@class='styles_comment__7_U0V']")).to_be_visible()
    # expect(page.locator("//div[@class='styles_wrap__1lgHX styles_selected__GWoli']")).to_be_visible()
    # expect(page.locator("//div[@class='styles_summary-content__3IqCA']")).to_be_visible()
    # page.click("//button[@class='btn dark narrow skip-min-width skip-padding v-space styles_primary-color__3fKw9']")
    # page.wait_for_timeout(2000)
    # expect(page.locator("//div[@class='styles_title__14p_x']")).to_be_visible()

    context.tracing.stop(path="/Users/zhekich/PycharmProjects/gepur_tests/gepur_automation_testing/gepur_automation_tests/test_add_product_and_checkot_user.zip")
    context.clear_cookies()
def test_add_product_and_checkout_user():
    with sync_playwright() as playwright:
        add_product_and_checkout(playwright)
