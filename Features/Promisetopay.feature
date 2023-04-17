# Created by Datasoft at 3/28/2023
Feature: samra

  Scenario:  Login & Redirect To Invoice Page
    Then User Navigates to Merchant Portal
    Then User Enters khanbro and SAmra1234
    Then User Clicks on Login Button
    Then Open Right Side Panel
    Then User Navigate To Invoice Tab
    Then click on Open
    Then take first invoice
    Then click on promise to pay button
    Then verify Ptop


#  Scenario: promise to pay
#    Then click on Open
#    Then take first invoice
