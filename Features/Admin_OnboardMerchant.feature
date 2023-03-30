Feature: I want to Onboard a new merchant

 Background:
   Then User Navigates to Admin Portal
   Then Enters Credentials NinjaTurtle and Talha123 and login into system
   Then Open Left Panel

 Scenario: Onboarding New Merchant
   Then Click On Onboard Merchants
   Then Click On Add Merchant
   Then Fill Onboard Merchant Form QA Automation Merchant, 15062347890, https://www.qa.com, dsqa@yopmail.com, 75080
   Then Select Business Type
   Then Select Industry
   Then Select Merchant Country
   Then Select Merchant State/Province
   Then Select Merchant City
   Then Select Merchant Currency
   Then Select Merchant Invoice Mode
   Then Select Merchant Status
   Then Enable Billing Center
   Then Upload Merchant Logo
   Then Save Merchant

 Scenario: Checking Filters
   Then Click On Onboard Merchants
   Then Click On Onboard Merchants Filters
   Then Select Entity Status In Filters (Onboard Merchant)
   #Then Select Merchant Country In Filters (Onboard Merchant)
   #Then Click Clear Filter Button (Onboard Merchant)
   #Then Click Apply Filter Button (Onboard Merchant)
