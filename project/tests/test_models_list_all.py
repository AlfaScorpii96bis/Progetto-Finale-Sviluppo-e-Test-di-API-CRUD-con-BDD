# tests/test_models.py
def test_list_all_products():
    products = Product.query.all()  # Ottiene tutti i prodotti
    assert len(products) > 0  # Assicura che ci siano almeno un prodotto
