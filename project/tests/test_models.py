# tests/test_models.py
def test_read_product():
    product = Product.query.first()  # Prende il primo prodotto nel database
    assert product is not None  # Verifica che il prodotto esista
    assert product.name == "Nome prodotto"  # Verifica che il nome del prodotto sia corretto
