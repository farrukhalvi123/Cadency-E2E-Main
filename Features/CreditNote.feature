# Created by Datasoft at 2/17/2023

Feature: abc

 Background: Login & Redirect To Invoice Page
    Then User Navigates to Merchant Portal
    Then User Enters khanbro and s3gxtMerqGtz
    Then User Clicks on Login Button
    Then Open Right Side Panel
    Then User Navigate To Invoice Tab


 Scenario: credit notes from invoice
   Then check if there are any open invoices
   Then click on Open
#   Then click on three dots and click to apply credit notes
#   Then enter values
#   Then get first CN no from text
