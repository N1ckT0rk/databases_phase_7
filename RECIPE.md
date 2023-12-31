Two Tables Design Recipe Template
Copy this recipe template to design and create two related database tables from a specification.

1. Extract nouns from the user stories or specification

As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

Nouns:

user account, email address, username, posts, title, content, number of views

2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

Record	Properties
users	email_address, username
posts	title, content, number of views

Name of the first table (always plural): users

Column names: email_address, username

Name of the second table (always plural): posts

Column names: title, content, number_of_views

3. Decide the column types
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

Table: users
id: SERIAL
email_address: text
username: text

Table: posts
id: SERIAL
title: text
content: text
number_of_views: init

4. Decide on The Tables Relationship
Most of the time, you'll be using a one-to-many relationship, and will need a foreign key on one of the two tables.

To decide on which one, answer these two questions:

Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No) Yes
Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No) No
You'll then be able to say that:

[A] has many [B]
And on the other side, [B] belongs to [A]
In that case, the foreign key is in the table [B]
Replace the relevant bits in this example with your own:

# EXAMPLE

1. Can one artist have many albums? YES
2. Can one album have many artists? NO

-> Therefore,
-> An artist HAS MANY albums
-> An album BELONGS TO an artist

-> Therefore, the foreign key is on the albums table.
If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).

Posts is the foreign key

5. Write the SQL
-- EXAMPLE
-- file: social_network.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email_address text,
  username text
);

-- Then the table with the foreign key second.
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
6. Create the tables
psql -h 127.0.0.1 social_network < social_network.sql
