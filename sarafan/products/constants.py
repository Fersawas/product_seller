MAX_LENGTH: int = 150
SLUG_LENGTH: int = 64

PRODUCT_VALIDATOR_MESSAGE: str = 'Цена не бможет быть меньше 1'

PRDOCUT_ERROR: dict = {
    'no product': 'Такого продукта не существует',
    'dublicate': 'Продукт уже добавлен в корзину',
    'not in shopcart': 'Продукта нет в корзине'
}

PRODUCT_CONFIRM: dict = {
    'product add': 'Товар добавлен в корзину'
}

SHOPPING_CART_ERROR: dict = {
    'empty': 'Ваша корзина пуста'
}
