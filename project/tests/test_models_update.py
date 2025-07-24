# tests/test_models.py
def test_update_product():
    product = Product.query.first()  # Prende il primo prodotto nel database
    product.name = "Nuovo nome prodotto"  # Modifica il nome
    product.save()  # Salva le modifiche
    updated_product = Product.query.first()  # Rilegge il prodotto
    assert updated_product.name == "Nuovo nome prodotto"  # Verifica che il nome sia stato aggiornato
