Feature: Login
  Scenario Outline: Login functionality
    Given I visit the guru99 Ecommerce website in Chrome
    When I click on ACCOUNT
    And I click on Login link
    And I enter <username> and <password>
    And I click on Login Button
    Then My Homepage should be displayed.

    Examples: Username & Password
    |username            | password |
    |testeight@email.com | test@12345|
