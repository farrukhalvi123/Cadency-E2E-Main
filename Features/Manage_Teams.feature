Feature: As a admin i want to Add a new Team

 Background:
   Then User Navigates to Admin Portal
   Then Enters Credentials Talhaadmin and Talha123 and login into system
   Then Open Left Side Panel & Click On Manage Teams

    @login
 Scenario Outline: Add New Team
      Given Click On Add New Team Button
      Then Enter Team Name & Description QA Team and This Is QA Team
      Then Goto Assign Users Tab
      Then Search User Kylian
      Then Check User is which Box (All Users)
      Then Move User Into Assign User
      Then Check User is which Box (Assigned User Box)
      Then Select Modules
      Then Save & Verify Team QA Team

      Examples:
      | Fname | Lname | AdminUname | PhnNum | Email | Pass | Cpass |
      | Kylian | Mbappe | NinjaTurtle | +923212323777 | ninja@yopmail.com | Talha123 | Talha123 |
