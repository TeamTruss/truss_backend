CREATE SCHEMA truss_data

create table office
(
  id BIGINT auto_increment,
  primary key (id),
  officeType TEXT not null,
  officeName TEXT not null,
  communication TEXT not null,
  price TEXT not null,
  result TEXT not null,
  keepingDeadline TEXT not null,
  afterService TEXT not null,
  satisfaction TEXT not null,
  description TEXT not null
);

create table person
(
  id BIGINT auto_increment,
  primary key (id),
  name TEXT not null,
  phoneNumber TEXT not null,
  type TEXT not null,
  location TEXT not null,
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
