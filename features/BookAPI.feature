# Created on 6/3/2026
Feature: Verify if books are added and deleted using Library API
    # Enter feature description here

    Scenario: Verify AddBook API functionality
        Given the book details which needs to be added to the Library
        When we execute the AddBook PostAPI method
        Then the book will be added successfully