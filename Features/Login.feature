# Created by Lenovo at 8/22/2022
@regression
Feature: As an end user i want to login to the cadency and view the dashboard page

 Background:
    Then User Logins with Main Credentials


    @login
 Scenario Outline: Invalid Login Scenarios to Cadency loginPage
      Then Click on Profile Thumbnail
      Then Logout
      Then User Enters <Uname> and <Pword>
      Then User Clicks on Login Button
      Then Verify User Navigation to HomePage or Error.

      Examples:
      | Uname | Pword |
      | abcxyz@data.com                     | abc xyz  |
      | samiullah.sadruddin@datasoft.com.pk | abc xyz|

    Scenario: Testing Logout
      Then Click on Profile Thumbnail
      Then Logout

#    Scenario: testing forgot password functionality     # will do this later
#      Then Click on Profile Thumbnail
#      Then Logout
#      Then click on forgot password
##      Then Enter farukhalvi1988@gmail.com to recover password
##      Then Click on Send button
#      Then Verify Forgot Password farukh_alvi88@hotmail.com
##      Then Fetch New OTP Code
#      Then Enter New Password
#      Then Enter Current Password
#      Then Click on Change password Button333









