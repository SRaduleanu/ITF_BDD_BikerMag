Feature: I want to search for products, add them to favorites list and add them to the cart
  @T9 @positiveTesting
    Scenario: I want to search for the cheapest product in a category and add it to favorites list
      Given I am logged into my account!
      When I search for the cheapest product
      When I add it to favorites
      Then Check for confirmation message

  @T10 @positiveTesting
    Scenario: I want to search for a product and add it to the cart
      Given I am logged in my account!
      When I search for a new product
      When I click on the product
      When I add the product to the cart
      Then I check the cart