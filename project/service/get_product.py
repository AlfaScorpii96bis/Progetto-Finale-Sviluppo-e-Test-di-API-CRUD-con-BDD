# service/routes.py
from flask import jsonify
from app.models import Product

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)  # Trova il prodotto con l'id fornito
    if product:
        return jsonify(product.to_dict())  # Restituisce i dettagli del prodotto
    return jsonify({"message": "Product not found"}), 404
