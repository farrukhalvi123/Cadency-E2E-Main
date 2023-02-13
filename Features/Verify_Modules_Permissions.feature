Feature: I want to Login with new user & verify permissions

 Background:
   Then User Navigates to Admin Portal
   Then Enters Cred NinjaTurtle and Talha123 and login into system
   Then Open Left Panel

 Scenario: Verifying Permissions
   Then Click On Dashboard
   Then Click On Onboard Merchants
   Then Click On Activity Logs
   Then Click On User Access Control
   Then Click On PAYMENT INTEGRATION

 Scenario: Verifying Dashboard Tiles
   Then Verify Onboarded Merchants Tile
   Then Verify Pending Merchants Tile
   Then Verify Total Users Tile
   Then Verify Total Teams Tile
   Then Verify Merchant Summary Tile
   Then Verify My Activities Tile
   Then Verify Merchant By Country Tile
   Then Verify My Task Tile

 Scenario: Verifying Onboard Merchant Options (Editing Not Allowed)
   Then Verify Edit option In Merchants

 Scenario: Verifying Activity Logs
  # Then Verify Data Of Labels
   Then Verify 1st Row Data