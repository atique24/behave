Feature: Registration

  Scenario Outline: New User Registration Functionality
    Given I visit the guru99 Ecommerce website in Chrome
    When I click on ACCOUNT
    And I click on Register
    And I provide the manadatory details <firstname>, <lastname>, <emailaddress>, <password>, <confirmpassword>
    And I click on Register button
    Then Registration is successfull.

    Examples:
      | firstname | lastname | emailaddress        | password   | confirmpassword |
      | Test      | one      | testeight@email.com | test@12345 | test@12345      |
      | Test      | two      | testnine@email.com  | test@12345 | test@12345      |









