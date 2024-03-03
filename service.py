import jsonpickle

import repository
from models import Product
from flask import make_response, request, jsonify


def read_products():
    products = repository.get_all()
    res = list()
    for product in products:
        print(product)
        res.append(Product(product_id=product[0], name= product[1],description=product[2],price=float(product[3])))

    return make_response(jsonpickle.dumps(res, make_refs=False, unpicklable=False))


def create_product():
    new_product = request.json
    product = Product(0, new_product['name'], new_product['description'], new_product['price'])
    id_created = repository.insert(product)
    product_created = Product(id_created, new_product["name"], new_product['description'], new_product['price'])
    return make_response(jsonpickle.dumps(product_created,make_refs=False, unpicklable=False))


def update_product(product_id: int):
    product_updated = request.json
    product = Product(product_id, product_updated['name'], product_updated['description'], product_updated['price'])
    product_id = repository.update_product(product)
    product_updated = Product(product_id, product_updated["name"], product_updated['description'], product_updated['price'])
    return make_response(jsonpickle.dumps(product_updated,make_refs=False, unpicklable=False))


def delete_product(product_id):
    product_id = repository.delete_product(product_id)
    res = dict({'id': product_id})
    return make_response(jsonify(message="success deleted", data=res))

