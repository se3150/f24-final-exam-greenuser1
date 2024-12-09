Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I enter "HELLO" in the message input
    And I set the shift value to "3"
    And I click the encode button
    Then I should see the result as "KHOOR"

  

Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I enter "KHOOR" in the message input
    And I set the shift value to "3"
    And I click tyhey decode button
    Then I should see the result as "HELLO"


