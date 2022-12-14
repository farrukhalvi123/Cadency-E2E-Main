# Created by Lenovo at 8/22/2022
@regression
Feature: As an end user i want to login to the cadency and view the dashboard page

#  Background:
#    Given Launch the Browser
When User is at login Page

    @login @smoke
#    Scenario: Successful login with valid scenarios
#    Then User Enters farukhalvi1988@gmail.com and 12345
#    Then User Clicks on Login Button

    @login
    Scenario Outline: Invalid Login Scenarios to Cadency loginPage
      Then Click on Profile Thumbnail
      Then Logout
      When User is at login Page
      Then User Enters <Uname> and <Pword>
      Then User Clicks on Login Button
      Then Verify User Navigation to HomePage or Error.
      Then Close the Browser

      Examples:
      | Uname | Pword |
      | abcxyz@data.com                     | abc xyz  |
      | samiullah.sadruddin@datasoft.com.pk | abc xyz|

    Scenario: Testing Logout
#      Then User Enters farukhalvi1988@gmail.com and 12345
#      Then User Clicks on Login Button
      Then Click on Profile Thumbnail
      Then Logout

    Scenario: testing forgot password functionality
      Then click on forgot password
#      Then Enter farukhalvi1988@gmail.com to recover password
#      Then Click on Send button
      Then Verify Forgot Password farukhalvi1988@gmail.com
      Then Fetch New OTP Code
      Then Enter New Password
      Then Enter Current Password
      Then Click on Change password Button





