CREATE TABLE users (
  id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  api_key VARCHAR ( 64 ) NOT NULL,
  enc_key VARCHAR ( 64 ) NOT NULL
);
INSERT INTO users (api_key, enc_key)
VALUES (
  '62c87a343ba883fbd8be60f82fee50a7a5d04f647866707521b29031ee55db61',
  '1be6ae0b28959a3e95b2d6e419aa7050e63f6b8b6d8d33223b7442aee5718978'
);
INSERT INTO users (api_key, enc_key)
VALUES (
  'b4a62ea61b142a5f98fa5990fcb7bae2259d3e18f40f4f265a3044e5e7337495',
  'b80c0227d8d934f881367980eb29770fc8220a65058bf89013ffbdd596ae0757'
);

CREATE TABLE secrets (
  id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  user_id INTEGER NOT NULL,
  content VARCHAR ( 256 ) NOT NULL
);
INSERT INTO secrets(user_id, content)
VALUES (1, 'tejctf{homebrew_hmac_is_a_bad_idea}');
INSERT INTO secrets(user_id, content)
VALUES (2, 'Test secret!');
