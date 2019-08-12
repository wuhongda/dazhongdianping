# dazhongdianping
破解大众点评WOFF字体反爬技术

爬取思路：  
1.根据request获取网页内容  
2.对网页进行解析发现字体和数字使用了WOFF字体加密   
3.通过对网页导入的WOFF字体文件进行解密    


执行过程：   
1·首先创建库->导入woff20190806.sql文件->根据database.py中的注释表结构创建表结构     
2.更改database.py中连接数据库的username password ip port等   
3.GetShopId.py->GetWoff.py->ShopDetail.py

爬取方法：    
1.每次需要根据网页内容中导入的Javascript找到对应的num和address所使用的woff字体文件.   
2.第一次需要自行构建字体库,在GetWoff脚本中有对应的表结构,其中position对应的为字体的点阵,每次更新时Unicode码会变化但点阵不会变化.   
3.将新的WOFF字体文件进行解析存库,然后与字库GetWoff脚本中对应的表做对比,对新表的word字段进行匹配.    
本文纯属技术联系和学习交流使用,严禁作为商业用途如有侵权联系作者删除  

![Image text](https://github.com/wuhongda/dazhongdianping/raw/master/数据截图/店铺信息截图.png)  
![Image text](https://github.com/wuhongda/dazhongdianping/raw/master/数据截图/店铺URL截图.png)  
![Image text](https://github.com/wuhongda/dazhongdianping/raw/master/数据截图/程序执行.png)  
![Image text](https://github.com/wuhongda/dazhongdianping/raw/master/数据截图/最终结果截图.png)   

欢迎技术宅一起学习交流有问题可邮件沟通
邮箱:hongda0812@163.com

