'''Проверка функции "Змінити кошик" '''

''' Given when user is on the main page 
    When When user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Одяг" button
    And user can click "Дивитися все" button
    And user can click "Size" button in any product to add in the cart
    And user can click "Кошик" button
    And user can see that product in the cart
    And user can see that size is the same as user choose
    And user can see that coast is the same as in product
    And user can click "Оформити замовлення" button
    And user can see checkout menu
    And user can clik "Змінити кошик" button
    And user can see product in the cart 
    And user can close a cart 
    Then user can see checkout menu '''




'''Проверка функции "Країна доставки" '''

''' Given when user is on the main page 
    When When user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Одяг" button
    And user can click "Дивитися все" button
    And user can click "Size" button in any product to add in the cart
    And user can click "Кошик" button
    And user can see that product in the cart
    And user can see that size is the same as user choose
    And user can see that coast is the same as in product
    And user can click "Оформити замовлення" button
    And user can see checkout menu
    And user can click in "Країна доставки" menu
    And user can see that "Україна" is chose automatically
    And user can see a message "При зміні країни доставки, знижки та бонуси можуть бути перераховані"
    And user can click "Пошук по країнам" menu
    And user can see "Пошук по країнам" menu
    And user can press "Close" button in "Пошук по країнам" menu
    Then user can see checkout menu '''




'''Проверка функции доставки'''

''' Given when user is on the main page 
    When When user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Одяг" button
    And user can click "Дивитися все" button
    And user can click "Size" button in any product to add in the cart
    And user can click "Кошик" button
    And user can see that product in the cart
    And user can see that size is the same as user choose
    And user can see that coast is the same as in product
    And user can click "Оформити замовлення" button
    And user can see checkout menu 
    And user see that "Самовивіз із відділення" is available
    And user can see options "Нова пошта" and "Укрпошта" 
    And user can click "Нова Пошта" button
    And user can see a fields that he available to input data on it
    And user can click "Зберегти" 
    And user can see that delivery data is saved
    And user can click "Укрпошта" button
    And user can see a fields that he available to input data on it
    And user can click "Зберегти" 
    And user can see that delivery data is saved
    And user can click "Кур'єр" button
    And user can click "Нова пошта кур'єр"
    And user can see all saved delivery data except street, number
    And user can input data in "Вулиця" field
    And user can input data in "Номер будинку" field 
    And user can input data in "Номер квартири" field
    And user can click "Зберегти" button 
    Then user can see that delivery data is saved '''




'''Проверка функций оплаты'''

''' Given when user is on the main page 
    When When user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Одяг" button
    And user can click "Дивитися все" button
    And user can click "Size" button in any product less than 1499 UAH to add in the cart
    And user can click "Кошик" button
    And user can see that product in the cart
    And user can see that size is the same as user choose
    And user can see that coast is the same as in product
    And user can click "Оформити замовлення" button
    And user can see checkout menu
    And user can choose "Нова пошта" delivery type
    And user can see than "Оплатити онлайн" button is selected
    And user can see "Оплата карткою - онлайн" and "Післяоплата" options
    And user can clik "Оплата карткою - онлайн" 
    And user can see that checkbox "Оплата карткою - онлайн" is selected
    And user can click "Післяоплата"
    And user can see that checkbox "Післяоплата" is selected
    And user can click "Інші способи" button
    And user can see "Оплата за рахунком" option
    And user can click "Оплата за рахунком"
    Then user can see that checkbox "Оплата за рахунком" is selected '''






'''Проверка поля Додати сертифікат'''

'''Given when user is on the main page 
    When When user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Одяг" button
    And user can click "Дивитися все" button
    And user can click "Size" button in any product less than 1499 UAH to add in the cart
    And user can click "Кошик" button
    And user can see that product in the cart
    And user can see that size is the same as user choose
    And user can see that coast is the same as in product
    And user can click "Оформити замовлення" button
    And user can see checkout menu 
    And user can click at "Додати сертифікат"
    And user can see "Сертифікат" field
    And user can input data at "Сертифікат" field
    And user can click "Застосувати" button
    Then user will see  '''





'''Проверка поля Промокод'''

''' Given when user is on the main page 
    When When user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Одяг" button
    And user can click "Дивитися все" button
    And user can click "Size" button in any product less than 1499 UAH to add in the cart
    And user can click "Кошик" button
    And user can see that product in the cart
    And user can see that size is the same as user choose
    And user can see that coast is the same as in product
    And user can click "Оформити замовлення" button
    And user can see checkout menu 
    And user can click at "Промокод"
    And user can see "Промокод" field
    And user can input data at "Промокод" field
    And user can click "Застосувати" button
    Then user will see  '''





'''Проверка поля Коментар до замовлення'''

'''Given when user is on the main page 
    When When user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Одяг" button
    And user can click "Дивитися все" button
    And user can click "Size" button in any product less than 1499 UAH to add in the cart
    And user can click "Кошик" button
    And user can see that product in the cart
    And user can see that size is the same as user choose
    And user can see that coast is the same as in product
    And user can click "Оформити замовлення" button
    And user can see checkout menu 
    And user can click "Коментар до замовлення" button
    And user can see "Додати коментар" field
    And user can input data in "Додати коментар" field
    And user can click "Зберегти" button
    Then user can see that text will be saved in "Коментар до замовлення" block '''




'''Проверка успешного оформления'''

''' Given when user is on the main page 
    When When user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Одяг" button
    And user can click "Дивитися все" button
    And user can click "Size" button in any product less than 1499 UAH to add in the cart
    And user can click "Кошик" button
    And user can see that product in the cart
    And user can see that size is the same as user choose
    And user can see that coast is the same as in product
    And user can click "Оформити замовлення" button
    And user can see checkout menu
    And user can choose delivery option "Нова пошта"
    And user can choose pay option "Оплата за рахунком"
    And user can see summary block with total price 
    And user can click "Оформити замовлення" button
    And user can see 
    '''






