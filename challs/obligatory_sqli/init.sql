CREATE TABLE users (
  id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  username VARCHAR ( 64 ) NOT NULL,
  password VARCHAR ( 64 ) NOT NULL
);
INSERT INTO users (username, password)
VALUES (
  'somejankylongusernamethatnobodywillguess',
  'somejankylongpasswordthatnobodywillguesseh?'
);

CREATE USER web WITH PASSWORD 'dummypassword';
GRANT CONNECT ON DATABASE postgres TO web;
GRANT USAGE ON SCHEMA public TO web;
GRANT SELECT ON users TO web;
