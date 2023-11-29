-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users cascade;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email_address text,
    username text
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (email_address, username) VALUES ('notreal@notreal.com', 'NotReal');
INSERT INTO users (email_address, username) VALUES ('defonotreal@defonotreal.com', 'DefoNotReal');

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then the table with the foreign key second.
-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    number_of_views int,

-- The foreign key name is always {other_table_singular}_id
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);



-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, content, number_of_views, user_id) VALUES ('faketitle', 'fakecontent', 0, 1);
INSERT INTO posts (title, content, number_of_views, user_id) VALUES ('faketitle2', 'fakecontent2', 0, 2);