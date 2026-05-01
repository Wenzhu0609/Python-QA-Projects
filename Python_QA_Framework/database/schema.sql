CREATE DATABASE IF NOT EXISTS PythonAutomation;

USE PythonAutomation;

CREATE TABLE IF NOT EXISTS CustomerInfo (
    CourseName VARCHAR(100),
    PurchasedDate VARCHAR(50),
    Amount INT,
    Location VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Books (
    name VARCHAR(255),
    isbn VARCHAR(50),
    aisle VARCHAR(50),
    author VARCHAR(255)
);
