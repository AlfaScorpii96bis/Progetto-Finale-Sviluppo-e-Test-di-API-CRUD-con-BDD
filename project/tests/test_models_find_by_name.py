# tests/test_models.py
def test_find_by_name():
    product = Product.query.filter_by(name="Nome prodotto").first()  # Cerca per nome
    assert product is not None  # Verifica che il prodotto esista
    assert product.name == "Nome prodotto"  # Verifica che il nome sia corretto
