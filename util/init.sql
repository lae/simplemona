DROP DATABASE IF EXISTS simplemona;
DROP DATABASE IF EXISTS simplemona_testing;
CREATE USER simplemona WITH PASSWORD 'testing';
CREATE DATABASE simplemona;
GRANT ALL PRIVILEGES ON DATABASE simplemona to simplemona;
-- Create a testing database to be different than dev
CREATE DATABASE simplemona_testing;
GRANT ALL PRIVILEGES ON DATABASE simplemona_testing to simplemona;
\c simplemona
CREATE EXTENSION hstore;
\c simplemona_testing
CREATE EXTENSION hstore;
