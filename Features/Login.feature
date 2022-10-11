# Created by Lenovo at 8/22/2022
@regression
Feature: As an end user i want to login to the cadency and view the dashboard page

  Background:
    Given Launch the Browser
    When User is at login Page

    @login @smoke
    Scenario: Successful login with valid scenarios
    Then User Enters farrukh.alvi@datasoft.com.pk and xSnbEu7eIjVJ
    Then User Clicks on Login Button

    @login
    Scenario Outline: Invalid Login Scenarios to Cadency loginPage
      Then User Enters <Uname> and <Pword>
      Then User Clicks on Login Button
      Then Verify User Navigation to HomePage or Error.
      Then Close the Browser

      Examples:
      | Uname | Pword |
      | abcxyz@data.com                     | abc xyz  |
      | samiullah.sadruddin@datasoft.com.pk | abc xyz|

    Scenario: Testing Logout
      Then User Enters farrukh.alvi@datasoft.com.pk and xSnbEu7eIjVJ
      Then User Clicks on Login Button
      Then Click on Profile Thumbnail
      Then Logout

#    Scenario: testing forgot password functionality
#      Then click on forgot password
#      Then Enter Email to recover password
#      Then Click on Send button
#      Then Verify Forgot Password Email
#      Then Fetch New OTP Code
#      Then Enter New Password
#      Then Enter Current Password
#      Then Click on Change password Button






