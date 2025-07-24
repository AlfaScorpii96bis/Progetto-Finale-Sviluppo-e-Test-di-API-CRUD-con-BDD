# tests/test_models.py
def test_find_by_category():
    product = Product.query.filter_by(category="Categoria prodotto").first()  # Cerca per categoria
    assert product is not None  # Verifica che il prodotto esista
    assert product.category == "Categoria prodotto"  # Verifica che la categoria sia corretta
