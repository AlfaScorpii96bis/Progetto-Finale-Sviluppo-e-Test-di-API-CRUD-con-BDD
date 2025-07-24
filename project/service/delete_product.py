# service/routes.py
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    db.session.delete(product)  # Elimina il prodotto
    db.session.commit()
    return jsonify({"message": "Product deleted"})
