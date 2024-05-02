// Получаем содержимое корзины из localStorage
var cart = JSON.parse(localStorage.getItem('cart')) || [];

// Функция для отображения содержимого корзины
function displayCart() {
    var cartItemsDiv = document.querySelector('.cart-items');
    var totalPriceSpan = document.querySelector('.total');

    cartItemsDiv.innerHTML = ''; // Очищаем содержимое корзины перед отображением
    var totalPrice = 0;

    // Перебираем товары в корзине
    cart.forEach(function(item) {
        var itemDiv = document.createElement('div');
        itemDiv.innerHTML = `
            <div class="Block_content col-12 col-sm-6 col-md-3">
                <p class="description">${item.name}</p>
                <p class="cost">Цена: ${item.price}</p>
                <button onclick="removeItem('${item.name}')">Удалить</button>
            </div>
        `;
        cartItemsDiv.appendChild(itemDiv);
        totalPrice += item.price;
    });

    // Обновляем общую стоимость на странице
    totalPriceSpan.textContent = 'Общая сумма: ' + totalPrice;
}

// Вызываем функцию отображения корзины при загрузке страницы
window.onload = displayCart;

// Функция для удаления товара из корзины
function removeItem(itemName) {
    // Находим индекс товара в корзине по его имени
    var index = cart.findIndex(item => item.name === itemName);

    // Удаляем товар из корзины
    if (index !== -1) {
        cart.splice(index, 1);
    }

    // Сохраняем обновленное содержимое корзины в localStorage
    localStorage.setItem('cart', JSON.stringify(cart));

    // Перезагружаем страницу для обновления корзины
    window.location.reload();
}

// Функция для оформления заказа (можно дополнить логикой)
function checkout() {
    alert('Ваш заказ оформлен!');
}
