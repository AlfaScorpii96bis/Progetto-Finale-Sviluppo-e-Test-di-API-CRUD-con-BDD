# features/products.feature
Feature: Elenco di tutti i prodotti

  Scenario: Elenco di tutti i prodotti
    Given che ci siano alcuni prodotti nel database
    When chiedo l'elenco di tutti i prodotti
    Then il sistema restituisce una lista di tutti i prodotti
