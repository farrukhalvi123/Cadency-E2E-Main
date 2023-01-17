# Created by Datasoft at 9/2/2022
Feature: As a admin i want to add a new invoice

  Background: Login & Redirect To Invoice Page
    Then User Navigates to Merchant Portal
    Then User Enters clarkkent and Cadency123!
    Then User Clicks on Login Button
    Then Open Right Side Panel
    Then User Navigate To Invoice Tab

  Scenario: Add Normal Invoice

    Then User Clicks On Add Invoice Button
    Then Add Customer
    Then Select Currency
    Then Verify Email is prefilled and disabled
    Then Verify Invoice Number is disabled
#    Then Select Exchange Rate
    Then Enter Reference
    Then Select InvoiceDate
    Then Select DueDate
    Then Select an Item
    Then click on Invoice Save Button
#    Then Verify Invoice has been Created

  Scenario: Add Existing Item in Invoices
    Then User Clicks On Add Invoice Button
    Then Add Customer
    Then Select Currency
    Then Verify Email is prefilled and disabled
    Then Verify Invoice Number is disabled
     Then Enter Reference
    Then Select InvoiceDate
    Then Select DueDate
    Then Select an Item
    Then Add Item This is test invoice description
    And Add Items Quantity
    And Adding Item Price
    And Adding Items Discount
    And Select Tax
    Then Verify Amount
    Then Verify Total Amount
    Then Click on Save Button
    Then Verify amount on detail page







