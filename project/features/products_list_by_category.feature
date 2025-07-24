# features/products.feature
Feature: Ricerca di un prodotto per categoria

  Scenario: Cercare un prodotto per categoria
    Given che ci siano alcuni prodotti nel database
    When cerco i prodotti per la categoria "Categoria 1"
    Then il sistema restituisce i prodotti della categoria "Categoria 1"
