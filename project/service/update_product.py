# service/routes.py
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    product.name = request.json['name']
    db.session.commit()  # Salva le modifiche
    return jsonify(product.to_dict())
