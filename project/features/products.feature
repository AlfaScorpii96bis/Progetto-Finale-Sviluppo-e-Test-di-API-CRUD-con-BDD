# features/products.feature
Feature: Lettura di un prodotto

  Scenario: Leggere un prodotto esistente
    Given che ci siano alcuni prodotti nel database
    When chiedo i dettagli del prodotto con ID 1
    Then il sistema restituisce il prodotto con ID 1
