# Created by samra  at 3/28/2023
Feature: samra
  Background:
    Then User Logins with Main Credentials
    Then Open Right Side Panel
    Then User Navigate To Invoice Tab
    Then Close Left Side Menu

  Scenario:  Login & Redirect To Invoice Page
    Then click on Open
    Then take first invoice
    Then click on promise to pay button
#    Then verify Ptop

  Scenario: in ALl tab identifying all promise to pay invoice
    Then User Navigate To Invoice Tab
    Then  identifying all ptop invoice with invoice no

  Scenario: promise fullfilled
    Then Duplicate an Invoice
    Then take first invoice
    Then click on promise to pay button
    Then go to new tab
    When user is at customer portal
    Then customer enter WD and tYXPthyjyS3V
    Then customer clicks login button
    Then going to invoice section from Cportal and towards open tab
    Then select country from dropdown
#    Then Payment method via paysafe
#    Then make a Payment SAMRA and 4111111111111111 and 5/25 and 856
  Scenario: Record Payment
    Then click on Open
    Then take first invoice
    Then click on promise to pay button
    Then Record Payment manually





