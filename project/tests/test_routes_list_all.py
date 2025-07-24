# tests/test_routes.py
def test_list_all_products(client):
    response = client.get('/products')  # GET per ottenere tutti i prodotti
    assert response.status_code == 200  # Verifica che la risposta sia OK
    assert len(response.json) > 0  # Verifica che ci siano prodotti nell'elenco
