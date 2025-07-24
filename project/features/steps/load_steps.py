# features/steps/load_steps.py
from behave import given
from app.models import Product, db

@given('che ci siano alcuni prodotti nel database')
def step_impl(context):
    product = Product(name="Prodotto 1", category="Categoria 1", availability=True)
    db.session.add(product)
    db.session.commit()
