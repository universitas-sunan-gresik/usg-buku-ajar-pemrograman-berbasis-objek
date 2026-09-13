CREATE DATABASE IF NOT EXISTS sip_usg;
USE sip_usg;

CREATE TABLE IF NOT EXISTS books (
    item_code VARCHAR(10) PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    author VARCHAR(100),
    isbn VARCHAR(20),
    publication_year INT,
    available BOOLEAN DEFAULT TRUE
);
