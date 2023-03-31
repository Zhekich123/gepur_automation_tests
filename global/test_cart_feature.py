

'''Проверка функции увеличения и уменьшения колличества товара'''

''' Given when user add product into a cart
    When user click "Plus" button
    And user can see that there are two products
    And user can click "Minus" button
    Then user can see that there are one product '''



'''Проверка изменения размера в корзине'''

''' Given when user add product into a cart
    When user click "Розмір" button
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

''' Given when user add two products into a cart
    When user click "Обрати все" button
    And user can see that checkboxes to the right of the product is selected
    And user can click one checkbox to the right of the product
    Then user can see that one product is selected '''




'''Проверка на удаление всех / частично товаров'''

''' Given when user add three products into a cart
    When user click one checkbox to the right of the product
    And user can see that checkbox to the right of the product is selected
    And user can click one "Trash" button
    And user can see the message "Ви дійсно хочете видалити 1 товар із кошика?"
    And user can click "Ні" button
    And user can see that selected product is still in the cart
    And user can click one "Trash" button
    And user can see the message "Ви дійсно хочете видалити 1 товар із кошика?"
    And user can click "Так" button
    And user can see that product is not in cart
    And user click "Обрати все" button
    And user can see that checkboxes to the right of the product is selected
    And user can click one "Trash" button
    And user can see the message "Ви дійсно хочете видалити 2 товара із кошика?"
    And user can click "Так" button
    Then user can see that cart is empty  '''


''' And user can click "Обрати все" button
    And user can see that checkboxes to the right of the product is selected
    And 
    And 
    And 
    And 
    And 
    And 
    And 
    And 
    And 
    Then  '''


'''Проверка на добавление всех / частично товаров в вишлист'''

