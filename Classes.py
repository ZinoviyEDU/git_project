# Задача4
# Необходимо создать модели работы со складскими запасами товаров и процесса оформления заказа этих товаров.
# Cписок требований:
# +++++ 1) Создайте товар с такими свойствами, как имя(name), подробные сведения(description or details),
# +++++ количество на складе(quantity), доступность(availability), цена(price).
# +++++ 2) Добавить товар на склад.
# +++++ 3) Удалить товар со склада
# +++++ 4) Распечатать остаток товара по его имени
# +++++ 5) Распечатать остаток всех товаров
# +++++ 6) Товар может принадлежать к категории
# +++++ 7) Распечатать список товаров с заданной категорией
# +++++ 8) Корзина для покупок, в которой может быть много товаров с общей ценой.
# +++++ 9) Добавить товары в корзину (вы не можете добавлять товары, если их нет в наличии)
# +++++ 10) Распечатать элементы корзины покупок с ценой и общей суммой
# +++++ 11) Оформить заказ и распечатать детали заказа по его номеру
# +++++ 12) Позиция заказа, созданная после оформления заказа пользователем.
# +++++ Он будет иметь идентификатор заказа(order_id), дату покупки(date_purchased), товары(items), количество(quantity)
# +++++ 13) После оформления заказа количество товара уменьшается на количество товаров из заказа.
#
#
# +++++ Добавить к этой задаче дескриптор для аттрибута цена.
# +++++ При назначении цены товара будет автоматически добавлен НДС 20%
# +++++ При получении цены товара, цена возврщается уже с учетом НДС

from datetime import datetime


class Nds:

    def __get__(self, instance, owner):
        return round(instance._price * 1.2, 2)

    def __set__(self, instance, value):
        instance._price = value


class Goods:
    price = Nds()

    def __init__(self, name: str, description: str = '', price: float = 0.00):
        self._name = name
        self._description = description
        self._quantity = 0
        self._availability = False
        self._price = price

    def __str__(self):
        return f'\t{self.name}:\n' \
               f'\t\tDescription: {self._description}\n' \
               f'\t\tQuantity: {self.quantity}\n' \
               f'\t\tAvailability: {self.availability}\n' \
               f'\t\tPrice: {self.price} UAH'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    # @name.deleter
    # def name(self):
    #     self._name = None

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self._quantity = quantity
        self._availability = True if self._quantity else False
        # if self._quantity:
        #     self._availability = True
        # else:
        #     self._availability = False

    @property
    def availability(self):
        return self._availability


class Warehouse:
    def __init__(self):
        self._categories = {}

    def add_goods(self, goods: Goods, quantity: int = 0, category: str = 'No category'):
        if isinstance(goods, Goods):
            if category not in self._categories:
                # print("param from add_goods - ", category)
                # print("self._categories - ", self._categories)
                self._categories[category] = []
            if goods in self._categories[category]:
                # print(goods)
                # print(self._categories[category])
                goods.quantity = goods.quantity + quantity
                # print(goods.quantity)
            else:
                self._categories[category].append(goods)
                goods.quantity = quantity
                # print(goods.quantity)
        else:
            print('"goods" must correspond to the "Goods" class')

    def delete_goods(self, goods: Goods):
        if isinstance(goods, Goods):
            for category, items in self._categories.items():
                if goods in items:
                    self._categories[category].pop(self._categories[category].index(goods))
                    print(f'Deleted "{goods.name}" from "{category}" category')
        else:
            print('"goods" must correspond to the "Goods" class')

    def print_the_rest_of_the_goods(self):
        for category, items in self._categories.items():
            print(f'Category: "{category}"')
            for item in items:
                print(item)
            print()

    def print_the_rest_of_the_goods_by_name(self, name: str):
        goods_flag = False
        for category, items in self._categories.items():
            for item in items:
                if item.name == name:
                    goods_flag = True
                    print(f'{name}: {item.quantity} pieces')
        if not goods_flag:
            print(f'Item named "{name}" is out of stock')

    def print_the_rest_of_the_goods_by_category(self, category: str):
        if category in self._categories:
            print(f'{category}:')
            for item in self._categories[category]:
                print(item)
        else:
            print(f'Categories named "{category}" do not exist')


class Cart:
    def __init__(self):
        self._goods = {}
        self._total_price = 0

    def add_goods(self, goods: Goods, quantity: int = 1):
        if isinstance(goods, Goods):
            if goods.quantity >= quantity:
                self._goods[goods] = quantity
                self._total_price += round(goods.price * quantity, 2)
            else:
                print(f'There is not enough product named "{goods.name}" in stock')
        else:
            print('"goods" must correspond to the "Goods" class')

    def print_basket_items(self):
        result = 'Goods in cart:\n' if self._goods else 'Cart is empty\n'
        for goods, quantity in self._goods.items():
            result += f'\t{goods.name}: {quantity} pieces X {goods.price} UAH = {round(goods.price * quantity, 2)} UAH\n'
        result += f'Total price: {self._total_price} UAH'
        print(result)

    def get_items(self):
        return self._goods


class Orders:
    def __init__(self):
        self.order_number = 0
        self.orders = {}

    def print_order_info(self, order_number: int):
        result = ''
        if order_number in self.orders:
            result += f'Order id: {order_number} \n' \
                      f'Purchase date: {self.orders[order_number]["date_purchased"]}\n' \
                      f'Items:\n'
            for item in self.orders[order_number]['items']:
                result += f'\t{item.name} - {self.orders[order_number]["items"][item]} pieces\n'
            print(result)
        else:
            print(f'Order with number "{order_number}" not found')

    def place_an_order(self, order: Cart):
        if isinstance(order, Cart):
            self.orders[self.order_number] = {'date_purchased': '{:%d.%m.%Y %H:%M}'.format(datetime.now()),
                                              'items': order.get_items()}
            print(f'Order is processed!')
            self.print_order_info(self.order_number)
            for item, value in self.orders[self.order_number]['items'].items():
                item.quantity -= value
            self.order_number += 1
        else:
            print('"Order" must correspond to the "Basket" class')


# TESTS
n1 = Goods('Paper', 'Paper description', 1)
# print(n1)
# print('Price with nds', n1.price)
# print('Price without nds', n1._price)

# # n1.availability = True
# # del n1.name
#
n2 = Goods('Glass', 'Glass description', 208.3)
# # print(n2)
# # print('Price with nds', n2.price)
# # print('Price without nds', n2._price)
#
n3 = Goods('Stone', 'Stone description', 33.89)
n4 = Goods('Earphones', 'Earphones description', 135.77)

f1 = Goods('Banana', 'Banana description', 22.5)
f2 = Goods('Pineapple', 'Pineapple description', 75.3)
f3 = Goods('Raspberry', 'Raspberry description', 33.3)
f4 = Goods('Mango', 'Mango description', 2.25)

m1 = Goods('STM32F103C8T6', 'STM32F103C8T6 description', 105.02)
m2 = Goods('STM32F407VET6', 'STM32F407VET6 description', 302.12)
m3 = Goods('STM32F407VGT6', 'STM32F407VGT6 description', 515.4)
m4 = Goods('STM32F768XFB4', 'STM32F768XFB4 description', 766.46)
#
warehouse = Warehouse()
cart = Cart()
orders = Orders()
#
warehouse.add_goods(n1, 30)


warehouse.add_goods(n2, 12)
warehouse.add_goods(n3)
warehouse.add_goods(n4)
warehouse.add_goods(f1, 25, 'Fruits')
warehouse.add_goods(f2, 70, 'Fruits')
warehouse.add_goods(f3, 33, 'Fruits')
warehouse.add_goods(f4, 50, 'Fruits')
# print(warehouse._categories)
# warehouse.delete_goods(f4)
# print(warehouse._categories)
warehouse.add_goods(m1, 22, 'Microcontrollers')
warehouse.add_goods(m2, 113, 'Microcontrollers')
warehouse.add_goods(m3, 77, 'Microcontrollers')
warehouse.add_goods(m4, 12, 'Microcontrollers')

# warehouse.print_the_rest_of_the_goods()
# warehouse.print_the_rest_of_the_goods_by_category("Fruits")
# warehouse.print_the_rest_of_the_goods_by_name("STM32F407VGT6")
# #
cart.add_goods(f1, 13)
cart.add_goods(n1, 13)
cart.add_goods(n2, 3)
cart.add_goods(n3, 26)
#
# cart.print_basket_items()
# print(cart.get_items())
# #
# #
orders.place_an_order(cart)
orders.place_an_order(cart)
orders.print_order_info(0)

