# Created by Lenovo at 8/23/2022
@regression
Feature: As an Admin User I want to Manage a new Customer

  Background: Login
    Then User Logins with Main Credentials
    Then Open Right Side Panel
    Then Go to Customer Tab
    Then Close Left Side Menu

  Scenario Outline: Add a Customer

#    Then Identify Number of Existing Customers
    Then Click on Add Button
    Then Verify Customer Email
    Then Add Customer Details <custom_disp_name> and <firsname> and <lsname> and <phone> and <website> and <ccemail>
    Then Select Customer currency
    Then Select Billing Centre
    Then Verify Toggle Active - InActive
    Then Upload Picture Logo
    And Click on Save Button
    Then Add Address Details <Street1> <street2> <pscode>
    And Click on Save Button
#    Then Select 50 Paging
    Then Identify Number of Existing Customers
#    Then Verify Details have been updated
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


  Scenario: Search Customer
    Then Search for Talha Bm DN and verify results


  Scenario: Verify Invoice Status and Tabs
    Then Search for Talha Bm DN and verify results
    Then View Customer Details
    Then Verify Invoice Tiles
    Then Verify Open Invoices
    Then Verify Closed Invoices
    Then Verify Invoices with Payments received
    Then Verify Credit Notes
    Then Verify Number of Tasks

  Scenario: Verify Customer Info
    Then Search for Talha Bm DN and verify results
    Then Verify Customer Details on Listing Page
    Then View Customer Details
#    Then Verify Customer Details on Details Page

  Scenario: Verify Invoice Current Amount
    Then Verify total amount on listing page against a customer
    Then View Customer Details
    Then Verify Customer Details on Details Page

  Scenario: Delete a Customer
    Then Select 50 Paging
    Then Click on 3 dots
    Then Click on Remove Customer
    Then Verify Customer has been removed


  Scenario: Verify Customer Amount on Listing page
    Then Verify Total amount against any customer
    Then View Customer Details
    Then Verify Total Amount on Detail Page

  Scenario: Verify Over Due Amount
    Then Enter Customer Selina Kyle into Search Field
    Then View Customer Details
#    Then Select 50 Paging
    Then Get Customer Balance
#    Then Verify it with Over Due Amount


