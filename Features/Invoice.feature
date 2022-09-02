# Created by Datasoft at 9/2/2022
Feature: As a admin i want to add a new invoice

  Scenario: Login & Redirect To Invoice Page
    Given Launch the Browser
    When User is at login Page
    Then User Enters samiullah.sadruddin@datasoft.com.pk and Unlimit3d
    Then User Clicks on Login Button
    Then User Navigate To Invoice Tab
    Then User Clicks On Add Invoice Button

#  Scenario : Add New Invoice
#
#    Then Add Customer
#    Then Select Currency
#    Then Select Exchange Rate
#    Then Enter Reference
#    Then Select InvoiceDate
#    Then Select DueDate
#    Then Close the Browser




