-- create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_db';
-- grant all privileges on hbnb_test_db database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- reload grant tables
FLUSH PRIVILEGES;
-- grant select on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- reload grant tables
FLUSH PRIVILEGES;
