Feature: Books capability

  Background:
    Given home: I am a user on home page
    When home: I click to bookstore application card
    When books: I click login button
    When login: I login with user criss and pass Test1234!

  @regression
  Scenario: I validate the stock count
    Then books: I validate that 8 books are displayed

  @regression
  Scenario Outline: I validate the search is working
    When books: I search after <query>
    Then books: I validate that only Git Pocket Guide book is displayed

  Examples:
    | query   |
    | Git     |
    | Richard |

  @regression
  Scenario: I validate that clear search is working
    When books: I search after test
    When books: I clear search input
    Then books: I validate that 8 books are displayed


