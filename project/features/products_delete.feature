# features/products.feature
Feature: Cancellazione di un prodotto

  Scenario: Cancellare un prodotto esistente
    Given che ci siano alcuni prodotti nel database
    When cancello il prodotto con ID 1
    Then il prodotto con ID 1 non esiste più nel sistema
