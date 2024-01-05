create table heart
(
  id bigint auto_increment,
  primary key (id),
  post_id BIGINT not null,
  foreign key(post_id) references post (id),
  user_id BIGINT not null,
  foreign key(user_id) references user (id)
);

create table user
(
  id bigint auto_increment,
  name text not null,
  role text not null
);

ALTER TABLE user CONVERT TO CHARACTER SET utf8mb4 COLLATE UTF8MB4_UNICODE_CI;
