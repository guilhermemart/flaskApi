class Product:
    id = 0
    name = ""
    description = ""
    price = 0

    def __init__(self, product_id, name, description, price):
        self.id = product_id
        self.name = name
        self.description = description
        self.price = price
