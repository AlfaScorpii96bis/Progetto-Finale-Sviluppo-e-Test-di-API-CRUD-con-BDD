# tests/test_routes.py
def test_read_product(client):
    # Simula una richiesta GET alla route /products/{id}
    response = client.get('/products/1')  # Supponiamo che il prodotto con id 1 esista
    assert response.status_code == 200  # Verifica che la risposta sia OK (200)
    assert 'name' in response.json  # Verifica che il nome del prodotto sia restituito
