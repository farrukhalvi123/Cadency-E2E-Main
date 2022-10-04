# Created by Datasoft at 9/2/2022
Feature: As a admin i want to add a new invoice

  Background: Login & Redirect To Invoice Page
    Given Launch the Browser
    When User is at login Page
    Then User Enters farrukh.alvi@datasoft.com.pk and xSnbEu7eIjVJ
    Then User Clicks on Login Button
    Then Open Right Side Panel
    Then User Navigate To Invoice Tab
    Then User Clicks On Add Invoice Button

  Scenario: Add Invoice
    Then Add Customer
    Then Select Currency
#    Then Select Exchange Rate
#    Then Enter Reference
#    Then Select InvoiceDate
#    Then Select DueDate
     Then Close the Browser





