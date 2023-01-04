Feature: As a admin i want to Check admin portal login Scenarios

 Background:
    Then User Navigates to Admin Portal

    @login
 Scenario Outline: valid Login Scenarios to Cadency loginPage

      Then Admin User Enters <Uname> and <Pword> and login into system
      Then Verify User Navigation to Dashboard or Not.
      Then Click on Admin Profile Thumbnail
      Then AdminLogout

      Examples:
      | Uname | Pword |
      | Talhaadmin | Talha123 |

 Scenario Outline: Incorrect Username & Correct Password Scenario

      Then Admin User Enters <Uname> and <Pword> and login into system
      Then Check Url after entering incorrect username

      Examples:
      | Uname | Pword |
      | Talhaadmin* | Talha1234 |

 Scenario Outline: Correct Username & InCorrect Password Scenario

      Then Admin User Enters <Uname> and <Pword> and login into system
      Then Check Url after entering incorrect password

      Examples:
      | Uname | Pword |
      | Talhaadmin | Talha123* |