# Created by Datasoft at 9/2/2022
Feature: As a admin i want to add a new invoice

  Background: Login & Redirect To Invoice Page
    Then User Navigates to Merchant Portal
    Then User Enters clarkkent and Cadency@123
    Then User Clicks on Login Button
    Then Open Right Side Panel
    Then User Navigate To Invoice Tab
    Then Close Left Side Menu

  Scenario: Add Normal Invoice

    Then User Clicks On Add Invoice Button
    Then Add Customer
    Then Select Currency
    Then Verify Email is prefilled and disabled
    Then Verify Invoice Number is disabled
    Then Enter Reference
    Then Select InvoiceDate
    Then Select DueDate
    Then Select an Item
    And Adding Item Price
    Then click on Invoice Save Button
#    Then Verify Invoice has been Created

  Scenario: Add Existing Item in Invoices
    Then User Clicks On Add Invoice Button
    Then Add Customer
    Then Select Currency
    Then Verify Email is prefilled and disabled
    Then Verify Invoice Number is disabled
    Then Enter Reference
    Then Select InvoiceDate
    Then Select DueDate
    Then Select an Item
    Then Add Item This is test invoice description
    And Add Items Quantity
    And Adding Item Price
    And Adding Items Discount
    And Select Tax
    Then Verify Amount
    Then Verify Total Amount
    Then Click on Save Button
    Then Verify amount on detail page

  Scenario: Search an Invoice with Invoice Name
    Then Enter Invoice Number in Search Field
    Then Verify Searched Invoice is Found

  Scenario: Search for Customer with Filter
    Then Enter Customer Selina Kyle into Search Field
    Then Select 50 Paging
    Then Verify list of customer name

  Scenario: Download Invoice PDF and Excel
    Then Select 50 Paging
    Then Click on Download Invoices in Excel
    Then Verify Downloaded CSV
    Then Click on PDF File Download
    Then Click on Download Invoices in PDF

  Scenario: Download one invoice
    Then Select Action Button

  Scenario: Verify Disputed Invoices
    Then Go to Disputed Tab and verify disputed invoices

  Scenario: Verify All Invoices
    Then Go to All Tab
    Then Verify Number of Invoices

  Scenario: Verify Open Invoices in Open Tab
    Then Go to Open Tab
    Then verify All Open Invoices

  Scenario: Verify Paid Invoices in Paid Tab
    Then Go to Paid Tab
    Then verify All Paid Invoices

  Scenario: Verify Partially Paid Invoices
    Then Go to Partially Paid Invoices
    Then Verify Partially Paid Invoices

  Scenario: Verify Waiting for Fund Invoices
    Then Go to Waiting for Funds Invoices
    Then Verify Waiting for Funds Invoice

  Scenario: Merchant duplicates an invoice
    Then Duplicate an Invoice

  Scenario: Delete an Invoice
    Then Click on More Options on an invoice
    Then Delete the Invoice

  Scenario: View and Verify Invoice Details
    Then Click on More Options on an invoice
    Then Click on View
    Then Verify Invoice Details

  Scenario: Edit Invoice from Detail Page
    Then Click on More Options on an invoice
    Then Click on View
    Then Click on Edit Invoice
    Then Edit Invoice from Detail Page
    Then Click on Save Button
    Then Verify Invoice Edited Successfully

  Scenario: Check Sending Email of Invoice
    Then Click on More Options on an invoice
    Then Click on View
    Then Verify Email Sending Details
    Then Send Email
    Then Verify Sent Email

  Scenario: Record Payment Against an Invoice
    Then Duplicate an Invoice
    Then Click on More Options on an invoice
    Then Click on View
    Then Click on Record Payment
    Then Record Payments

  Scenario: Record Full Payment Against Invoice
    Then Duplicate an Invoice
    Then Click on More Options on an invoice
    Then Click on View
    Then Click on Record Payment
    Then Record Full Payments
#    Then Verify Sent Email and attachment

  Scenario: Record Half Payment Against Invoice
    Then Duplicate an Invoice
    Then Click on More Options on an invoice
    Then Click on View
    Then Click on Record Payment
    Then Record Payments
#    Then Verify Sent Email and attachment

  Scenario: Send Invoice Reminder
    Then Duplicate an Invoice
    Then Click on More Options on an invoice
    Then Click on View
    Then Click on Send Reminder
    Then Verify Email Sending Details
    Then Send Email


  Scenario:   Dispute an Invoice from Main Portal
    Then Duplicate an Invoice
    Then Click on More Options on an invoice
    Then Click on View
    Then Get Invoice Number and Customer Name
    Then Click on Dispute Icon
    Then Verify Invoice Number
    Then Verify Customer Name
    Then Select reason to dispute
    Then Add amount to dispute
    Then Add a note
    Then Click on Save Button

  Scenario: Export Invoice PDF from Detail Page.
    Then Duplicate an Invoice
    Then Click on More Options on an invoice
    Then Click on View
    Then Click on Export Invoice and verify exported text
#    Then Verify Exported Invoice Details










