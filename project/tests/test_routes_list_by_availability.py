# tests/test_routes.py
def test_list_by_availability(client):
    response = client.get('/products?availability=true')  # GET per cercare i prodotti per disponibilità
    assert response.status_code == 200  # Verifica che la risposta sia OK
    assert all(product['availability'] is True for product in response.json)  # Verifica che tutti i prodotti siano disponibili
