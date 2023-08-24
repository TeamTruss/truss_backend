CREATE SCHEMA truss_data

create table builder
(
  id BIGINT auto_increment,
  primary key (id),
  name TEXT not null,
  sotong TEXT not null,
  price TEXT not null,
  sigongResult TEXT not null,
  dateJunsu TEXT not null,
  afterService TEXT not null,
  satisfaction TEXT not null,
  description TEXT not null,
);

create table constructor
(
  id BIGINT auto_increment,
  primary key (id),
  name TEXT not null,
  sotong TEXT not null,
  price TEXT not null,
  sigongResult TEXT not null,
  dateJunsu TEXT not null,
  afterService TEXT not null,
  satisfaction TEXT not null,
  description TEXT not null,
);

create table person
(
  id BIGINT auto_increment,
  primary key (id),
  name TEXT not null,
  phoneNumber TEXT not null,
  type TEXT not null,
  agree BOOLEAN
);



create table building
(
  id bigint auto_increment,
  primary key (id),
  name TEXT,
  src TEXT,
  price TEXT,
  description TEXT,
  rate FLOAT,
  like_num INT,
  date TEXT,
  office BIGINT not null,
  builder BIGINT not null
);
