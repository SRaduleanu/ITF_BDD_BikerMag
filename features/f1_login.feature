Feature: Check that the login button on the BikerMag website is working properly
  @T1 @positiveTesting
    Scenario: I am on BikerMag website and I want to accept the Cookies
      Given I am accessing the BikerMag website
      Then Click Sunt de Acord

  @T2 @negativeTesting
    Scenario Outline: Trying to login using an invalid password
      Given I am on the BikerMag homepage and I want to initiate the login process with invalid password
      When I click on "Intra in cont" button
      When I enter my valid email
      When I enter my invalid password "<password>"
      When I click on "Intra in cont" authentication button
      Then I receive an "<error_message>"
      Examples:
        |password|error_message|
        |piramide|Adresa de e-mail / parola introduse sunt incorecte. Te rugam sa incerci din nou.|
        |serban123|Adresa de e-mail / parola introduse sunt incorecte. Te rugam sa incerci din nou.|
        |321rsn123|Adresa de e-mail / parola introduse sunt incorecte. Te rugam sa incerci din nou.|

  @T3 @positiveTesting
    Scenario: I am on BikerMag website and I want to initiate the login process with the valid password
      When I click on "Intra in cont" button
      When I enter my valid email
      When I enter my valid password
      When I click on "Intra in cont" authentication
      Then I am redirected to my account page

  @T4 @positiveTesting
    Scenario: I am logged into my BikerMag account and I want to logout
      When I check to see if I am logged in
      When I click on my account
      When I click on logout
      Then I check to see if I am no longer logged in

