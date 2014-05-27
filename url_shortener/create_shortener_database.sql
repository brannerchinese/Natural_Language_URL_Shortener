-- ******************
-- 20140527
--
-- Script to populate URL-shortener database
--
-- Run as 
--     sqlite3 shortener.db < create_shortener_database.sql
--
-- ******************

DROP TABLE IF EXISTS shortened_to_url;
CREATE TABLE shortened_to_url (
    shortened TEXT PRIMARY KEY UNIQUE,
    -- We don't care if URLs are not unique.
    url TEXT
);

-- Report what the database contains.
SELECT * FROM sqlite_master WHERE type='table';
