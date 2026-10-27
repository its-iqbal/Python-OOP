class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.__stock = stock

    def get_info(self):
        return(f"Name: {self.name} | Price: {self.price} | Stock: {self.__stock}")

class Laptop(Product):
    def __init__(self, name, price, stock, ram):
        super().__init__(name, price, stock)
        self.ram = ram

    def get_info(self):
        return(f"{super().get_info()} | RAM: {self.ram}")

class Shoe(Product):
    def __init__(self, name, price, stock, size):
        super().__init__(name, price, stock)
        self.size = size

    def get_info(self):
        return(f"{super().get_info()} | Size: {self.size}")

class Store:
    def __init__(self):
        self.inventory = []

    def add_item(self, product):
        self.inventory.append(product)

    def print_catalog(self):
        for item in self.inventory:
            if isinstance(item, Laptop):
                print(f"{item.get_info()} | Details -- TECH DEPT 💻")
            elif isinstance(item, Shoe):
                print(f"{item.get_info()} | Details -- APPAREL DEPT 👟")

lap  = Laptop("Dell Latitude", 150000, 15, "16GB")
sho = Shoe("Nike", 90000, 20, 6)

store = Store()

store.add_item(lap)
store.add_item(sho)

store.print_catalog()