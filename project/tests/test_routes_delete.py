# tests/test_routes.py
def test_delete_product(client):
    response = client.delete('/products/1')  # DELETE per eliminare il prodotto con id 1
    assert response.status_code == 200  # Verifica che la risposta sia OK
    assert response.json['message'] == 'Product deleted'  # Verifica che il messaggio di successo sia restituito
