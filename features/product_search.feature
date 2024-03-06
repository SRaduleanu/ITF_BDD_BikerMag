Feature: I want to search for products using the search bar and using the filters
  @T4 @positiveTesting
    Scenario: I want to search for products using the search bar
      Given I am logged in my account
      When I type the product in the search bar
      When I click on the search button
      Then The search results are displayed containing "Toate produsele"