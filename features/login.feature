Feature: Login capability

  Background:
    Given home: I am a user on home page
    When home: I click to bookstore application card
    When books: I click login button


  @smoke
  Scenario Outline: I login with invalid credentials
    When login: I login with user <user> and pass <pswd>
    Then login: I validate that error message is displayed

  Examples:
    | user    | pswd      |
    | criss   | Test1234  |
    | crisp   | Test1234  |


  @regression
  Scenario: I login with valid credentials
    When login: I login with user criss and pass Test1234!
    Then books: I should land on books page


