from datetime import datetime

class InventoryError(Exception):
    pass


class OutOfStockError(InventoryError):
    def __init__(self, name, available):
        self.name = name
        self.available = available
        super().__init__(f"{name}: only {available} items available")


class ItemNotFoundError(InventoryError):
    pass


def log_error(error):
    now = datetime.now()
    try:
        with open("error_msg.txt", "a") as f:
            f.write(f"{now} - {error}\n")
    except Exception as e:
        print(f"Failed to log error: {e}")


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, qty):
        if qty <= 0:
            raise ValueError("Quantity must be positive")

        self.items[name] = self.items.get(name, 0) + qty

    def remove_item(self, name, qty):
        if name not in self.items:
            raise ItemNotFoundError(f"Item not found: {name}")

        if qty <= 0:
            raise ValueError("Quantity must be positive")

        if qty > self.items[name]:
            raise OutOfStockError(name, self.items[name])

        self.items[name] -= qty


inventory = Inventory()

# Add items
inventory.add_item("Football", 10)
inventory.add_item("Bat", 5)

# Test errors
try:
    inventory.add_item("Pencil", 0) 
except ValueError as e:
    log_error(e)

try: 
    inventory.remove_item("Football", 15)
except OutOfStockError as e:
    log_error(e)
except InventoryError as e:
    log_error(e)

try:
    inventory.remove_item("Laptop", 1)
except ItemNotFoundError as e:
    log_error(e)
except InventoryError as e:
    log_error(e)