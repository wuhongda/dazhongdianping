from fontTools.ttLib import TTFont
import requests
import random
import Database as db
import re
user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
]
#request 请求头部、由于此脚本请求不同的网页header信息不一致所以未设置全局变量
#解析woff字体库的数字类型
#主函数入口
def main():
    headers = {'User-Agent': random.choice(user_agent),  # 随机选取头部代理,防止被屏蔽
               'Connection': "keep-alive",
               'Host': "www.dianping.com",
               'referer': 'http://www.dianping.com/',
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
               }
    #随机选取一家店铺获取WOFF文件
    sql="select shophref from dzcomment_shop  ORDER BY RAND() LIMIT 1;"
    result=db.select_data(sql)
    if len(result)>0:
        url="http://"+result[0]
        try:
            r = requests.get(url, headers=headers)
            r.encoding = 'utf-8'
            #print(r.text)
            #print(url)
            woff_url = re.findall('//s3plus.meituan.net/v1/(.*?)"', r.text, re.S)
            r.close()
            #print(woff_url)
            if(len(woff_url)>0):
                result_url="https://s3plus.meituan.net/v1/"+woff_url[0]
                get_woff_file(result_url)
                return 1
            else:
                return "URL IS NULL"
        except Exception as e:
            print(e)
            return 0
    else:
        return 0
#获取address和num对应的woff文件URL
def get_woff_file(url):
    headers = {'User-Agent': random.choice(user_agent),  # 随机选取头部代理,防止被屏蔽
               'Connection': "keep-alive",
               'Host': "s3plus.meituan.net",
               'referer': 'http://www.dianping.com/',
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
               }
    #print("ING..........")
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    numwoff = re.findall('@font-face{font-family: "PingFangSC-Regular-num(.*?).woff', r.text, re.S)
    addresswoff = re.findall('@font-face{font-family: "PingFangSC-Regular-address(.*?).woff', r.text, re.S)
    savewoff(numwoff,'num.woff')
    savewoff(addresswoff,'address.woff')
#将获取的woff文件保存到本地便于解析存放点阵信息到数据库
def savewoff(woff,filename):
    headers = {'User-Agent': random.choice(user_agent),  # 随机选取头部代理,防止被屏蔽
               'Connection': "keep-alive",
               'Host': "s3plus.meituan.net",
               'referer': 'http://www.dianping.com/',
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
               }
    result = ''
    for tmp in woff:
        result = result + tmp
    woff2 = re.findall('url\(\"//(.*?);', result, re.S)
    resultb = ''
    for a in woff2:
        resultb = resultb + str(a).replace('eot', 'woff').replace(')', '').replace('"', '')
    #print(resultb)
    url = "https://" + resultb
    response_woff = requests.get(url, headers=headers).content
    with open(filename, 'wb') as f:
        f.write(response_woff)
    save_word(filename)
#解析woff字体文件进行解析
def save_word(filename):
    tablename=filename.replace('.woff','')+"_dic_tmp"
    font = TTFont(filename)
    glyf = font.get('glyf')
    result = font['cmap']
    sql_delete="truncate table %s"%(tablename)
    db.inset_data(sql_delete)
    cmap_dict = result.getBestCmap()
    for key, value in cmap_dict.items():
        k_tmp = str(hex(eval(str(key))))
        b = k_tmp.replace("0x", '')
        glyf = font.get('glyf')
        c = glyf[value]
        sql_insert = "insert into %s (name,ten_key,sixteen_key,position) values (\'%s\',%s,\'%s\',\'%s\')" % ( tablename,value, key, b, c.coordinates)
        db.inset_data(sql_insert)
if __name__ == '__main__':
    main()

#在执行完此函数之后需要执行几条SQL语句进行更新当前字库
#update address_dic_tmp a ,woff20190806 b set a.word=b.word  where a.position=b.position;
#update num_dic_tmp a ,woff20190806 b set a.word=b.word  where a.position=b.position;
#insert into woff_dic select  * from  num_dic_tmp  where word  in ('0','1','2','3','4','5','6','7','8','9');
#insert into woff_dic select  * from  address_dic_tmp where word not in ('0','1','2','3','4','5','6','7','8','9');
