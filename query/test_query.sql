CREATE SCHEMA truss_data;

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

create table user
{ 
  id BIGINT auto_increment,
  primary key (id),
  name TEXT not null,
  email TEXT not null
};

create table post
(
  id BIGINT auto_increment,
  primary key (id),
  title TEXT not null,
  text TEXT not null,
  pictures TEXT not null,
  author TEXT not null,
  created_at DATETIME not null DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME not null DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  category TEXT not null,
  thumbnail TEXT not null,
  likeCount BIGINT not null,
  viewCount BIGINT not null,
  comments TEXT not null
);

create table house
(
  id BIGINT auto_increment,
  primary key (id),
  title TEXT not null,
  image TEXT not null,
  subImage1 TEXT not null,
  subImage2 TEXT not null,
  buildingImage TEXT not null,
  blueprint TEXT not null,
  costImage TEXT not null,
  officeImage TEXT not null,
  price BIGINT not null,
  floorSpace BIGINT not null,
  roomNumber BIGINT not null,
  toiletNumber BIGINT not null,
  hasLoft BOOLEAN not null
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


ALTER TABLE builder CONVERT TO CHARACTER SET utf8mb4 COLLATE UTF8MB4_UNICODE_CI;
ALTER TABLE building CONVERT TO CHARACTER SET utf8mb4 COLLATE UTF8MB4_UNICODE_CI;
ALTER TABLE office CONVERT TO CHARACTER SET utf8mb4 COLLATE UTF8MB4_UNICODE_CI;
ALTER TABLE post CONVERT TO CHARACTER SET utf8mb4 COLLATE UTF8MB4_UNICODE_CI;
ALTER TABLE house CONVERT TO CHARACTER SET utf8mb4 COLLATE UTF8MB4_UNICODE_CI;