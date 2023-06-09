Feature: As a admin i want to Add a new user

 Background:
   Then User Navigates to Admin Portal
   Then Enters Credentials Talhaadmin and Talha123 and login into system
   Then Open Left Side Panel

    @login
 Scenario Outline: Add New User
      Given Click On Add New User Button
      Then Add User Details <Fname> and <Lname> and <AdminUname> and <PhnNum> and <Email> and <Pass> and <Cpass>
      Then Click On Teams DD
      Then Select Team Test
      Then Select UserType DD
      Then Select User Status
      Then Save

      # Enable Two Factor Authentication & Reset Auth QR Code Will be test manually

      Examples:
      | Fname | Lname | AdminUname | PhnNum | Email | Pass | Cpass |
      | Kylian | Mbappe | NinjaTurtle | +923212323777 | ninja@yopmail.com | Talha123 | Talha123 |

  Scenario: Check user exist
      Given Enter text in search field Kylian
      Then Verify Username if Already Exist

  Scenario: Clear Filter Button
       Given Enter text in search field Lorem Ispum Is Dummy Text
       Then Verify No Record Found Text
       Then Click Clear Filter Button
       Then Verify Some Record

  Scenario: Verify Filters
       Then Click On Filter Icon
       Then Select User Status Filter Option (Active)
       Then Select Filter By Team Test
       Then Click on Apply Button
       Then Check Filter Results
       Then Make User Inactive
       Then Click On Filter Icon
#       Then Select User Status Filter Option (InActive)
#       Then Select Filter By Team Test
#       Then Click on Apply Button
#       Then Check Filter Results
