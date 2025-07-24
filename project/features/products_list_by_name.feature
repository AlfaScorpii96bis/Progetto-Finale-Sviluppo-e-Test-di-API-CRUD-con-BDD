# features/products.feature
Feature: Ricerca di un prodotto per nome

  Scenario: Cercare un prodotto per nome
    Given che ci siano alcuni prodotti nel database
    When cerco il prodotto con nome "Prodotto 1"
    Then il sistema restituisce il prodotto con nome "Prodotto 1"
