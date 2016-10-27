echo \
'
create database if not exists mymem;
use mymem;
create table if not exists memdata (
    id int unsigned not null auto_increment primary key,
    question text,
    answer text,
    familiar int,
    type char (50),
    last_modify_time datetime
);
' | mysql -uroot
