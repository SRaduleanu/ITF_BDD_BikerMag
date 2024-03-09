Feature: I want to check that I can add a delivery address in My account
  @T7 @positiveTesting
    Scenario: Adding a new delivery address in My account
      Given I am logged into My account
      When I click on Adrese
      When I click on Adauga adresa noua
      When I fill in the address necessary fields
      When I click on Salveaza
      Then I verify that the address was saved successfully

  @T8 @positiveTesting
    Scenario: Deleting a delivery address
      Given I am logged into the account
      When I click on Adrese menu
      When I click on Stergere
      Then I verify that the address was deleted successfully
