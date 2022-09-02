# Created by Lenovo at 8/23/2022
@regression
Feature: As an Admin User I want to Manage a new Customer
  Background:
    Given Launch the Browser
    When User is at login Page
    Then User Enters samiullah.sadruddin@datasoft.com.pk and Unlimit3d
    Then User Clicks on Login Button

  Scenario Outline: Add a Customer
    Then Go to Customer Tab
    Then Click on Add Button
    Then Verify Customer Number
    Then Add Customer Details <custom_disp_name> and <firsname> and <lsname> and <phone> and <mail> and <website> and <ccemail>
    Then Verify Toggle Active - InActive
    Then Upload Picture Logo
    Then Add Address Details <Street1> <street2> <pscode>
    And Click on Save Button
    Then Verify New User has been added
#    Then Verify Details have been updated
    Then Close the Browser
    Examples:
    |custom_disp_name|firsname|lsname|phone|mail|website|ccemail|Street1 | street2| pscode|
    |Farrukh Doe|Farrukh|Alvi|03404456789|fja@jaf.com|https://www.gmail.com |fja@jaf.com| teststreet123!@#| teststreet2##@| 123456|
  @edit_customer
  Scenario: Edit Customer
    Then Go to Customer Tab
    Then Click on 3 dots and open edit customer form
    Then Verify Toggle Active - InActive
    Then Edit Customer Details
    Then Verify Details have been updated

  Scenario: Apply Filters and verify data
    Then Go to Customer Tab
    Then click on Filter
    Then Select Country
    Then Verify Filter is applied


