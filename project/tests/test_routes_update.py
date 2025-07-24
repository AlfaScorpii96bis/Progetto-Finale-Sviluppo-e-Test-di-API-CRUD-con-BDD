# tests/test_routes.py
def test_update_product(client):
    response = client.put('/products/1', json={'name': 'Nuovo nome prodotto'})  # PUT per aggiornare
    assert response.status_code == 200  # Verifica che la risposta sia OK
    assert response.json['name'] == 'Nuovo nome prodotto'  # Verifica che il nome sia stato aggiornato
