function addToCart(name, price) {
    var item = {
        name: name,
        price: parseFloat(price)  // Конвертируем цену в число с плавающей точкой
    };

    // Получаем текущее содержимое корзины из localStorage, если оно есть
    var cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Добавляем товар в корзину
    cart.push(item);

    // Сохраняем обновленное содержимое корзины в localStorage
    localStorage.setItem('cart', JSON.stringify(cart));

    // Перенаправляем пользователя на страницу корзины
    window.location.href = "/basket";
}
