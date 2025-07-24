import pytest
import requests  # O usa Flask's test client se stai usando Flask

BASE_URL = "http://localhost:5000/api/products"  # URL dell'API, sostituisci con l'endpoint corretto

def test_read_product():
    # Supponiamo di voler leggere un prodotto con un ID specifico
    product_id = 1
    response = requests.get(f"{BASE_URL}/{product_id}")

    # Verifica che la risposta abbia uno status code 200 (OK)
    assert response.status_code == 200

    # Verifica che i dati restituiti contengano le informazioni corrette (in base alla struttura dei dati)
    data = response.json()
    assert 'id' in data
    assert data['id'] == product_id
    assert 'name' in data
    assert 'price' in data
    # Aggiungi altre asserzioni in base ai dati che ti aspetti

