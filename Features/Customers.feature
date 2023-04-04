# Created by Lenovo at 8/23/2022
@regression
Feature: As an Admin User I want to Manage a new Customer

  Background: Login
    Then User Navigates to Merchant Portal
    Then User Enters clarkkent and Cadency@123
    Then User Clicks on Login Button
    Then Open Right Side Panel
    Then Go to Customer Tab

  Scenario Outline: Add a Customer

#    Then Identify Number of Existing Customers
    Then Click on Add Button
    Then Verify Customer Email
    Then Add Customer Details <custom_disp_name> and <firsname> and <lsname> and <phone> and <website> and <ccemail>
    Then Select Customer currency
    Then Verify Toggle Active - InActive
    Then Upload Picture Logo
    And Click on Save Button
    Then Add Address Details <Street1> <street2> <pscode>
    And Click on Save Button
    Then Identify Number of Existing Customers
    Then Verify Details have been updated
    Examples:
    |custom_disp_name|firsname|lsname|phone|website|ccemail|Street1 | street2| pscode|
    |Farrukh Doe|Farrukh|Alvi|+923404456789|https://www.gmail.com |fja@jaf.com| teststreet123!@#| teststreet2##@| 123456|


  @edit_customer
  Scenario: Edit Customer
    Then Click on 3 dots and open edit customer form
    Then Verify Toggle Active - InActive
    Then Verify Currency Selected and Disabled
    Then Edit Customer Details
    Then Verify Details have been updated

  Scenario: Apply Filters and verify data
    Then click on Filter
    Then Select Country
    Then Select Invoice Status
    Then Verify Filter is applied
    Then Verify Invoices with Current Status

  Scenario: Search Customer
    Then Search for Selina Kyle and verify results


  Scenario: Verify Invoice Status and Tabs
    Then Search for Selina Kyle and verify results
    Then View Customer Details
    Then Verify Invoice Tiles
    Then Verify Open Invoices
    Then Verify Closed Invoices
    Then Verify Invoices with Payments received
    Then Verify Credit Notes
    Then Verify Number of Tasks

  Scenario: Verify Customer Info
    Then Search for Selina Kyle and verify results
    Then Verify Customer Details on Listing Page
    Then View Customer Details
    Then Verify Customer Details on Details Page





