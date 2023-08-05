CREATE SCHEMA truss_data

create table builder
(
  id bigint auto_increment,
  name TEXT not null,
  url TEXT not null,
  constraint test_pk
    primary key (id)
);
