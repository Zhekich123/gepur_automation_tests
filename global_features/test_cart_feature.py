

'''Проверка функции увеличения и уменьшения колличества товара'''

''' Given user is on the main page 
    When user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Одяг" button
    And user can click "Дивитися все" button
    And user can click any size to "Додати до кошика" any product 
    And user can click "Кошик" button
    And user can see that product is on the cart
    And user can click "Plus" button
    And user can see that there are two products
    And user can click "Minus" button
    Then user can see that there are one product '''



'''Проверка изменения размера в корзине'''

''' Given user is on the main page 
    When user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Одяг" button
    And user can click "Дивитися все" button
    And user can click any size to "Додати до кошика" any product 
    And user can click "Кошик" button
    And user can see that product is on the cart
    And user can click "Розмір" button
    And user can see "Змірити розмір" functions 
    And user can click "S" button
    And user can see that size is changed
    And user can click "Розмір" button
    And user can see "Змірити розмір" functions 
    And user can click "M" button
    And user can see that size is changed
    And user can click "Розмір" button
    And user can see "Змірити розмір" functions 
    And user can click "L" button
    And user can see that size is changed
    And user can click "Розмір" button
    And user can see "Змірити розмір" functions 
    And user can click "XL" button
    Then user can see that size is changed '''



'''Проверка на выбор всех / частично товаров'''

''' Given user is on the main page 
    When user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Одяг" button
    And user can click "Дивитися все" button
    And user can click any size to "Додати до кошика" two random products 
    And user can click "Кошик" button
    And user can see that products is on the cart
    And user can click "Обрати все" button
    And user can see that checkboxes to the right of the products is selected
    And user can click one checkbox to the right of the any product
    Then user can see that another product is selected '''




'''Проверка на удаление всех / частично товаров'''

''' Given user is on the main page 
    When user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Одяг" button
    And user can click "Дивитися все" button
    And user can click any size to "Додати до кошика" to add three any products
    And user can click "Кошик" button
    And user can see that products is on the cart
    And user can click one checkbox to the right of the one product
    And user can see that checkbox to the right of the one product is selected
    And user can click one "Trash" button
    And user can see the message "Ви дійсно хочете видалити 1 товар із кошика?"
    And user can click "Ні" button
    And user can see that selected product is still in the cart
    And user can click one "Trash" button
    And user can see the message "Ви дійсно хочете видалити 1 товар із кошика?"
    And user can click "Так" button
    And user can see that product is not in cart
    And user click "Обрати все" button
    And user can see that checkboxes to the right of the products is selected
    And user can click one "Trash" button
    And user can see the message "Ви дійсно хочете видалити 2 товара із кошика?"
    And user can click "Так" button
    Then user can see that cart is empty  '''




'''Проверка на добавление всех / частично товаров в вишлист'''

''' Given user is on the main page 
    When user point mouse on sidebar menu on home page
    And user can see "Menu" 
    And user can click "Одяг" button
    And user can click "Дивитися все" button
    And user can click any size to "Додати до кошика" to add three any products
    And user can click "Кошик" button
    And user can see that products is on the cart
    And user can click one checkbox to the right of the one product
    And user can see that checkbox to the right of the one product is selected
    And user can click "Обране" button
    And user can see the message "Ви дійсно хочете перемістити 1 товар до обраного?"
    And user can click "Ні" button
    And user can see that selected product is still in the cart
    And user can click "Обране" button
    And user can see the message "Ви дійсно хочете перемістити 1 товар до обраного?"
    And user can click "Так" button
    And user can see that product added into a wishlist
    And user click "Обрати все" button
    And user can see that checkboxes to the right of the products is selected
    And user can click "Обране" button
    And user can see the message "Ви дійсно хочете перемістити 2 товара до обраного?"
    And user can click "Так" button
    Then user can see that products added into a wishlist '''

