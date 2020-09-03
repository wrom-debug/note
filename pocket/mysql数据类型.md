# 数据表 {ignore}

---
[toc]

* 无符号    unsigned
* 默认  default
* 唯一  unique(字段)
    1. 可以多个字段联合不唯一
* 主键  primary key     （非空唯一）
    1. 没有指定第一个非空唯一就是
    2. 也可多个字段联合主键
* 自增  auto_increment
    1. 必须唯一
    2. 对数字
    3.自带非空
* 非空  not null
* 单选 enum
* 多选 set
* 指定小数位 decimal（长度，小数位）
* 外键 foreign key(字段) references 表名(字段)
    1. 后接on update cascade(关联记录更改外键也更改)
    2. 外表字段唯一
