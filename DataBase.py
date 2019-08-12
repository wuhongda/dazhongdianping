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
       
自建字库 word字段为不变信息 每次根据position去匹配
woff20190806
Create Table: CREATE TABLE `woff20190806` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL DEFAULT '0' COMMENT 'unicode字符名称',
  `ten_key` varchar(256) NOT NULL DEFAULT '0' COMMENT '十进制字符',
  `sixteen_key` varchar(256) NOT NULL DEFAULT '0' COMMENT '十六进制字符',
  `position` text NOT NULL COMMENT 'x，y轴描点坐标',
  `word` varchar(10) NOT NULL DEFAULT '' COMMENT '对应的解密字体',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1807 DEFAULT CHARSET=utf8


用于存放地址信息的woff字体文件
Create Table: CREATE TABLE `address_dic_tmp` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL DEFAULT '0' COMMENT 'unicode字符名称',
  `ten_key` varchar(256) NOT NULL DEFAULT '0' COMMENT '十进制字符',
  `sixteen_key` varchar(256) NOT NULL DEFAULT '0' COMMENT '十六进制字符',
  `position` text NOT NULL COMMENT 'x，y轴描点坐标',
  `word` varchar(10) NOT NULL DEFAULT '' COMMENT '对应的解密字体',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=603 DEFAULT CHARSET=utf8
1 row in set (0.00 sec)

用于存放num信息的woff字体文件
CREATE TABLE `num_dic_tmp` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL DEFAULT '0' COMMENT 'unicode字符名称',
  `ten_key` varchar(256) NOT NULL DEFAULT '0' COMMENT '十进制字符',
  `sixteen_key` varchar(256) NOT NULL DEFAULT '0' COMMENT '十六进制字符',
  `position` text NOT NULL COMMENT 'x，y轴描点坐标',
  `word` varchar(10) NOT NULL DEFAULT '' COMMENT '对应的解密字体',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=588 DEFAULT CHARSET=utf8


将两者进行结合每次仅需要在一张表进行匹配数据
CREATE TABLE `woff_dic` (
  `id` int(20) NOT NULL,
  `name` varchar(30) NOT NULL DEFAULT '0' COMMENT 'unicode字符名称',
  `ten_key` varchar(256) NOT NULL DEFAULT '0' COMMENT '十进制字符',
  `sixteen_key` varchar(256) NOT NULL DEFAULT '0' COMMENT '十六进制字符',
  `position` text NOT NULL COMMENT 'x，y轴描点坐标',
  `word` varchar(10) NOT NULL DEFAULT '' COMMENT '对应的解密字体'
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.00 sec)

'''