# Created by samra  at 3/28/2023
Feature: samra
  Background:
   Then User Navigates to Merchant Portal
    Then User Enters khanbro and SAmra1234
    Then User Clicks on Login Button
    Then Open Right Side Panel

  Scenario:  Login & Redirect To Invoice Page
    Then User Navigate To Invoice Tab
    Then click on Open
    Then take first invoice
    Then click on promise to pay button
#    Then verify Ptop

  Scenario: in ALl tab identifying all promise to pay invoice
    Then User Navigate To Invoice Tab
    Then  identifying all ptop invoice with invoice no



