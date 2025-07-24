# features/products.feature
Feature: Ricerca di un prodotto per disponibilità

  Scenario: Cercare un prodotto disponibile
    Given che ci siano alcuni prodotti nel database
    When cerco i prodotti disponibili
    Then il sistema restituisce solo i prodotti disponibili
