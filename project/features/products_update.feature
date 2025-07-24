# features/products.feature
Feature: Aggiornamento di un prodotto

  Scenario: Aggiornare un prodotto esistente
    Given che ci siano alcuni prodotti nel database
    When aggiorno il prodotto con ID 1
    Then il sistema restituisce il prodotto con ID 1 con il nuovo nome
