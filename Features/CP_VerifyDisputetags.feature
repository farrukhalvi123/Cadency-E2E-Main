# Created by Datasoft at 3/17/2023
Feature: Open customer portal and search for anyone invoive from "Invoices" marked as 'disputed' & 'open'
  and verify this thing on 'Account statemnet'
 Background:
   When user is at customer portal
   Then customer enter ransom and a45GnsKuzYs4
   Then customer clicks login button

  Scenario: go to invoices, and pick any invoice with status disputed and open
    When customer at dashboard and hover over side panel and click invoice option
    Then search dispute tagged invoice and save the catched inv number

