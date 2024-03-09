Feature: I want to search for products using the search bar and using the filters
  @T5 @positiveTesting
    Scenario: I want to search for products using the search bar
      Given I am logged in my account
      When I type the product in the search bar
      When I click on the search button
      Then The search results are displayed containing "Toate produsele"

  @T6 @positiveTesting
    Scenario: I want to use the filters after using the search bar
      When I search for a product
      When I click on a category
      When I click on the desired size
      Then The filter results are displayed

