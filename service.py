import jsonpickle

import repository
from models import Product
from flask import make_response, request


def read_products():
    products = repository.get_all()
    res = list()
    for product in products:
        res.append(Product(product_id=product[0], name= product[1],description=product[2],price=product[3]))
    return make_response(jsonpickle.dumps(res, make_refs=False, unpicklable=False))


def create_product():
    new_product = request.json
    product = Product(0, new_product['name'], new_product['description'], new_product['price'])
    id_created = repository.insert(product)
    return f"product {id_created} created"


def update_product(product_id: int):
    product_updated = request.json
    product = Product(product_id, product_updated['name'],product_updated['description'],product_updated['price'])
    product_id = repository.update_product(product)
    return f"product {product_id} updated"


def delete_product(product_id):
    product_id = repository.delete_product(product_id)
    return f"product {product_id} deleted"
