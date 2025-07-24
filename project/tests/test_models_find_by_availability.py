# tests/test_models.py
def test_find_by_availability():
    product = Product.query.filter_by(availability=True).first()  # Cerca per disponibilità
    assert product is not None  # Verifica che il prodotto esista
    assert product.availability is True  # Verifica che il prodotto sia disponibile
