DROP DATABASE IF EXISTS sql5717327;
CREATE DATABASE sql5717327;
USE sql5717327;

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    unix_id VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    moniker VARCHAR(10) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    department VARCHAR(255)
);