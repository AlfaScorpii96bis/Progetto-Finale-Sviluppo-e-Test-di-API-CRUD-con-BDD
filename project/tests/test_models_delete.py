# tests/test_models.py
def test_delete_product():
    product = Product.query.first()  # Prende il primo prodotto
    product.delete()  # Elimina il prodotto
    deleted_product = Product.query.first()  # Verifica se il prodotto è stato eliminato
    assert deleted_product is None  # Assicura che non ci siano più prodotti
