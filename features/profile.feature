Feature: Profile capability

  @temp
  Scenario Outline: I add/remove books to my collection
    Given home: I am a user on home page
    When home: I click to bookstore application card
    When books: I click login button
    When login: I login with user criss and pass Test1234!
    When books: I add to collection the book title <book1>
    When books: I add to collection the book title <book2>
    When menu: I click profile_section
    Then profile: Book with title <book1> is present in collection
    Then profile: Book with title <book2> is present in collection
    When profile: I remove the book with title <book1> from collection
    Then profile: Book with title <book1> is NOT present in collection
    Then profile: Book with title <book2> is present in collection
    When profile: I remove the book with title <book2> from collection
    Then profile: Book with title <book2> is NOT present in collection

  Examples:
    | book1            | book2               |
    | Git Pocket Guide | Speaking JavaScript |