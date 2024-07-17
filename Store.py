#Создай класс Store:
#-Атрибуты класса:
#name: название магазина.
#address: адрес магазина.
#items: словарь, где ключ - название товара, а значение - его цена. Например,
# {'apples': 0.5, 'bananas': 0.75}.
#Методы класса:
#__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
#-  метод для добавления товара в ассортимент.
#метод для удаления товара из ассортимента.
#метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
#метод для обновления цены товара.

class Store():
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.items =  {}

    def add_item(self, item_name, price):
        self.items[item_name] =price
        print(f"товар {item_name} был добавлен в {self.name}")

    def remove(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"товар {item_name} был удален в {self.name}")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, price):
        if item_name in self.items:
            self.items[item_name] = price
            print(f" цена на товар {item_name} обновлена  {self.name}")
        else:
            print(f"товар не найден")

store1 = Store("продукты", "Маркса, 22" )
store2 = Store("праздник", "Маркса, 23" )
store3 = Store("промтовары", "Маркса, 25" )

store1.add_item("хлеб", 57)
store1.add_item("молоко", 77)
store1.add_item("яйца", 88)

store1.remove('хлеб')

print(store1.get_price('молоко'))
store1.update_price("яйца", 90)