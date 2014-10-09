drop table if exists Users;
drop table if exists Role;

create table Role (
   id integer primary key,
   name char(20) unique not null
);

insert into Role VALUES (1, "Manager");
insert into Role values (2, "Waiter");
insert into Role values (3, "Kitchen Assistant");

create table Users (
   id integer primary key,
   uname char(12) unique not null,
   password char(60) not null,
   role integer not null,
   foreign key(role) references Role(name)
);

insert into Users (uname, password, role) VALUES
   ('manager', '$2a$12$CyLyLDPA5NFTY48o3fANQOEsni38JgHBk3FNwdUFd1OwYMBZxN146', 1);
