# tests/test_routes.py
def test_list_by_category(client):
    response = client.get('/products?category=Categoria')  # GET per cercare i prodotti per categoria
    assert response.status_code == 200  # Verifica che la risposta sia OK
    assert all('Categoria' in product['category'] for product in response.json)  # Verifica che tutti i prodotti abbiano la categoria "Categoria"
