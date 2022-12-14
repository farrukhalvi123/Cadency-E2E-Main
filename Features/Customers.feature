# Created by Lenovo at 8/23/2022
@regression
Feature: As an Admin User I want to Manage a new Customer
  Background:
    Given Launch the Browser
    When User is at login Page
    Then User Enters farukhalvi1988@gmail.com and 12345
    Then User Clicks on Login Button

  Scenario Outline: Add a Customer
    Then Open Right Side Panel
    Then Go to Customer Tab
    Then Click on Add Button
    Then Verify Customer Email
    Then Add Customer Details <custom_disp_name> and <firsname> and <lsname> and <phone> and <website> and <ccemail>
    Then Select Customer currency
    Then Verify Toggle Active - InActive
    Then Upload Picture Logo
    Then Add Address Details <Street1> <street2> <pscode>
    And Click on Save Button
    Then Verify New User has been added
#    Then Verify Details have been updated
    Examples:
    |custom_disp_name|firsname|lsname|phone|website|ccemail|Street1 | street2| pscode|
    |Farrukh Doe|Farrukh|Alvi|+923404456789|https://www.gmail.com |fja@jaf.com| teststreet123!@#| teststreet2##@| 123456|


  @edit_customer
  Scenario: Edit Customer
    Then Open Right Side Panel
    Then Go to Customer Tab
    Then Click on 3 dots and open edit customer form
    Then Verify Toggle Active - InActive
    Then Verify Currency Selected and Disabled
    Then Edit Customer Details
    Then Verify Details have been updated

  Scenario: Apply Filters and verify data
    Then Open Right Side Panel
    Then Go to Customer Tab
    Then click on Filter
    Then Select Country
    Then Verify Filter is applied


