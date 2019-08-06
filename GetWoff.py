from fontTools.ttLib import TTFont
import requests
import  string
import datetime
import Database as db
def main():
    font = TTFont('0805.woff')
    glyf=font.get('glyf')
    result=font['cmap']
    cmap_dict = result.getBestCmap()
    for key,value in cmap_dict.items():
        k_tmp = str(hex(eval(str(key))))
        b = k_tmp.replace("0x", '')
        glyf = font.get('glyf')
        c=glyf[value]
        sql="insert into woff20190806(name,ten_key,sixteen_key,position) values (\'%s\',%s,\'%s\',\'%s\')"%(value, key, b, c.coordinates)
        print(sql)
        #result=db.inset_data(sql)
if __name__ == '__main__':
    result=main()


    '''
    CREATE TABLE `woff20190806` (
        `id` int(20) NOT NULL AUTO_INCREMENT,
        `name` varchar(256) NOT NULL DEFAULT '0' COMMENT 'unicode字符名称',
        `ten_key` varchar(256) NOT NULL DEFAULT '0' COMMENT '十进制字符',
        `sixteen_key` varchar(256) NOT NULL DEFAULT '0' COMMENT '十六进制字符，其中就是网页对应的内容，在前边加上&#x
        `position` text NOT NULL COMMENT 'x，y轴描点坐标',
        `word` varchar(10) NOT NULL DEFAULT '' COMMENT '对应的解密字体',
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=1807 DEFAULT CHARSET=utf8              
    '''


