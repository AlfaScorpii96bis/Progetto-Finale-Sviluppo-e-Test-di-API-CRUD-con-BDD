# tests/factories.py
import factory
from app.models import Product  # Immagina che "Product" sia il modello di prodotto

class ProductFactory(factory.Factory):
    class Meta:
        model = Product  # Collega il prodotto al modello di prodotto vero

    name = factory.Faker('name')  # Genera un nome casuale
    category = factory.Faker('word')  # Categoria casuale
    price = factory.Faker('random_number', digits=3)  # Prezzo casuale
    availability = factory.Faker('boolean')  # Disponibilità casuale (vero o falso)
