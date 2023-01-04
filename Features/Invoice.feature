# Created by Datasoft at 9/2/2022
Feature: As a admin i want to add a new invoice

  Background: Login & Redirect To Invoice Page
    Then User Navigates to Merchant Portal
    Then User Enters farukh_alvi88@hotmail.com and 9ntUIsAv8imS
    Then User Clicks on Login Button

  Scenario: Add Normal Invoice
    Then Open Right Side Panel
    Then User Navigate To Invoice Tab
    Then User Clicks On Add Invoice Button
    Then Add Customer
    Then Select Currency
    Then Verify Email is prefilled and disabled
    Then Verify Invoice Number is disabled
#    Then Select Exchange Rate
    Then Enter Reference
    Then Select InvoiceDate
    Then Select DueDate
    Then Add an Item
    Then click on Invoice Save Button





