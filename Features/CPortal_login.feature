# Created by Datasoft at 1/3/2023
Feature: just want to login cadency customer portal
  # Enter feature description here
Background:
   When user is at customer portal

    @login
    Scenario: Valid login on customer portal
      Then customer enter ransom and a45GnsKuzYs4
      Then customer clicks login button
