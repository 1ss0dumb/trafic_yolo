-- 1. 库的操作
-- 删库
DROP DATABASE IF EXISTS TrafficsDB;
-- 建库
CREATE DATABASE IF NOT EXISTS TrafficsDB DEFAULT CHARACTER SET utf8;
-- 切换库
use TrafficsDB;

-- 2. 表的操作
-- 删除表 - 用户表
drop table if EXISTS TUser;
-- 建表 - 用户表
CREATE TABLE TUser(
	u_id varchar(12) not null primary key,
	u_name varchar(30) not null default ""
);

-- 删除表 - 监控日志表
drop table if EXISTS TLogs;
-- 建表 - 监控日志表
CREATE TABLE TLogs(
	l_id int auto_increment primary key,
	l_x int default 0,
    l_y int default 0,
    l_w int default 0,
    l_h int default 0,
    l_prob float default 0.0,
    l_clsid int default 0,
    l_clsname varchar(30) 
);
-- 数据初始化：基线数据
insert into TUser(u_id, u_name) values('WU0001', 'YangQiang');
insert into TUser(u_id, u_name) values('WU0002', 'ZhengLi');
insert into TUser(u_id, u_name) values('WU0003', 'ZhangYuantong');
insert into TUser(u_id, u_name) values('WU0004', 'ZhouYan');
insert into TUser(u_id, u_name) values('WU0005', 'Ming');
commit;
-- insert into TLogs(l_x, l_y, l_w, l_h, l_prob, l_clsid, l_clsname) values(1, 2, 3, 4, 1.0, 0, 'YangQiang');
-- commit;