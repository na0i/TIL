-- CREATE TABLE classmates (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   name TEXT NOT NULL,
--   age INT NOT NULL,
--   address TEXT NOT NULL
-- );

CREATE TABLE users(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  age INTEGER,
  country VARCHAR(50),
  phone VARCHAR(20),
  balance INTEGER
);