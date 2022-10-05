# Created by Datasoft at 9/2/2022
Feature: As a admin i want to add a new invoice

  Background: Login & Redirect To Invoice Page
    Given Launch the Browser
    When User is at login Page
    Then User Enters farukh_alvi88@hotmail.com and 12345
    Then User Clicks on Login Button
    Then Open Right Side Panel
    Then User Navigate To Invoice Tab
    Then User Clicks On Add Invoice Button

  Scenario: Add Invoice
    Then Add Customer
    Then Select Currency
    Then Verify Email is prefilled and disabled
    Then Verify Invoice Number is disabled
#    Then Select Exchange Rate
#    Then Enter Reference
    Then Select InvoiceDate
    Then Select DueDate
    Then Add an Item
     Then Close the Browser





