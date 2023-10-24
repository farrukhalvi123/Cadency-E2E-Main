Feature: I want to Login with new user & verify permissions

 Background:
   Then Admin Enters Login Credentials

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

 Scenario: Verifying Activity Logs (Only View Works, No Del & Edit functionality)
#   Then Verify View & Delete
#   Then Verify Labels
