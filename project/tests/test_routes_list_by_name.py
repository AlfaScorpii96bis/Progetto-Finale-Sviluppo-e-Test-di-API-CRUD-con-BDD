# tests/test_routes.py
def test_list_by_name(client):
    response = client.get('/products?name=Prodotto')  # GET per cercare i prodotti per nome
    assert response.status_code == 200  # Verifica che la risposta sia OK
    assert all('Prodotto' in product['name'] for product in response.json)  # Verifica che tutti i prodotti abbiano "Prodotto" nel nome
