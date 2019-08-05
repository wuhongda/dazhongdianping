# coding:utf-8
import MySQLdb
def inset_data(sql):
    db = MySQLdb.connect("xxxxx", "xxx", "xxx", "xx", charset='utf8')  # 根据自己的情况设置ip/database/username/password
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()
        return 1
    except :
        return 0
def select_data(sql): #由于自身习惯擅长处理list类型 所有返回list类型
    db = MySQLdb.connect("xxxxx", "xxx", "xxx", "xx", charset='utf8')  # 根据自己的情况设置ip/database/username/password
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        result_list=[]
        for row in results:
            result_list.append(row[0])
        return result_list
    except:
        return "error"
if __name__ == '__main__':
    pass
'''表结构信息
    店铺URL及分类信息表
    CREATE TABLE `dzcomment_shop` (
        `id` int(10) NOT NULL AUTO_INCREMENT,
        `shopid` int(20) NOT NULL COMMENT '店铺对应ID',
        `shophref` varchar(256) NOT NULL COMMENT '店铺对应的URL',
        `tag` varchar(40) NOT NULL COMMENT '美食分类',
        `status` int(4) DEFAULT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=49603 DEFAULT CHARSET=utf8
       
    商家信息表 
    CREATE TABLE `shop_detail` (
        `id` int(10) NOT NULL AUTO_INCREMENT,
        `shopid` int(20) NOT NULL COMMENT '店铺ID',
        `name` varchar(256) NOT NULL DEFAULT '-1' COMMENT '店铺名称',
        `tag` varchar(256) NOT NULL COMMENT '美食类型',
        `region` varchar(256) NOT NULL COMMENT '行政区',
        `area` varchar(256) NOT NULL COMMENT '商圈',
        `avg` varchar(30) NOT NULL COMMENT '人均消费',
        `flavor` varchar(30) NOT NULL COMMENT '口味',
        `envir` varchar(30) NOT NULL COMMENT '环境',
        `service` varchar(30) NOT NULL COMMENT '服务',
        PRIMARY KEY (`id`),
        UNIQUE KEY `shopid` (`shopid`)  部分美食属于多种分类 
        ) ENGINE=InnoDB AUTO_INCREMENT=2632 DEFAULT CHARSET=utf8
'''