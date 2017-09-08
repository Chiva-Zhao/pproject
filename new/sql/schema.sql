CREATE DATABASE grab;
USE grab;

create table xueqiu_base
(
  uid varchar(255) null comment '雪球id',
  title varchar(255) null comment '标题',
  author varchar(255) null comment '作者',
  category varchar(255) null comment '分类',
  time varchar(255) null comment '文章时间',
  `read` varchar(255) null comment '阅读',
  priase varchar(255) null comment '点赞',
  forward varchar(255) null comment '转发',
  comment varchar(255) null comment '评论数量',
  url varchar(255) null comment '文章地址',
  create_time varchar(255) null comment '抓取时间'
)
  comment '雪球基础表'
;

create table xueqiu_author_white
(
  id int auto_increment
    primary key,
  author varchar(255) null comment '作者名字',
  uid varchar(255) null comment '作者雪球id'
)
  comment '雪球作者白名单'
;

create table xueqiu_author_black
(
  id int auto_increment
    primary key,
  author varchar(255) null comment '作者名字',
  uid varchar(255) null comment '作者雪球id'
)
  comment '雪球作者黑名单'
;

create table xueqiu_article_day
(
  title varchar(255) null comment '标题',
  author varchar(255) null comment '作者',
  time varchar(255) null comment '文章时间',
  priase varchar(255) null comment '点赞',
  forward varchar(255) null comment '转发',
  comment varchar(255) null comment '评论数量',
  url varchar(255) null comment '文章地址',
  create_time varchar(255) null comment '抓取时间'
)
  comment '雪球每日文章'
;


create table xueqiu_article_best
(
  title varchar(255) null comment '标题',
  author varchar(255) null comment '作者',
  url varchar(255) null comment '文章地址',
  create_time varchar(255) null comment '抓取时间'
)
  comment '雪球每日最佳文章'
;

