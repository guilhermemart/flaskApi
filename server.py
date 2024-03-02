from flask import Flask
import service


def setup_router():
    app = Flask(__name__)
    app.add_url_rule("/products", view_func=service.read_products, methods=['GET'])
    app.add_url_rule("/product", view_func=service.create_product, methods=['POST'])
    app.add_url_rule("/product/<product_id>", view_func=service.update_product, methods=['PUT'])
    app.add_url_rule("/product/<product_id>", view_func=service.delete_product, methods=['DELETE'])
    return app
