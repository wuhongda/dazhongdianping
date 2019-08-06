#coding:utf-8
import requests
import random
import re
import threading
import time
import Database as db
from lxml import etree
g_lock=threading.Lock() #定义锁

#代理浏览器header
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
#request 请求头部
headers = {'User-Agent': random.choice(user_agent),  # 随机选取头部代理,防止被屏蔽
           'Connection': "keep-alive",
           'Host': "www.dianping.com",
           'referer': 'http://www.dianping.com/',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
           }
#解析woff字体库的数字类型
word={
    'x':'.',
    'e719':'1',
    'ef77':'2',
    'f200':'3',
    'ef11':'4',
    'efab':'5',
    'e887':'6',
    'e594':'7',
    'f537':'8',
    'ecb6':'9',
    'e32b':'0',
}
hreflist=[]#全局请求URL列表

class GetShopInfo(threading.Thread):

    #获取均价信息
    def get_avg(self,avglist):
        clist=''
        for k in avglist:
            b = str(k)
            c = b.replace('<d class="num">', ' ').replace('</d>', ' ').replace('&#x', ' ').replace(';', ' ')
            clist = c.split(' ')
            #print(clist)
        s = ''
        #print(clist)
        for k in clist:
            try:
                if len(k) == 4:
                    tmp = word[k]
                else:
                    tmp = str(k)
                s = s + str(tmp)
            except:
                pass
        return s
    #获取店铺名称信息
    def get_name(self,shopname):
        ar=''
        try:
            for a in shopname:
                #print(a)
                al = a.split('【')[1]
                ar = al.split('】')[0]
            return ar
        except IndexError:
            pass
    #或许点评分数信息
    def get_comment(self,comment_score):
        alist = []
        blist = []
        all_list = []
        #print(comment_score)
        try:
            for i in range(3):
                a = comment_score[i]
                alist.append(a)
            for k in alist:
                b = str(k)
                c = b.replace('<d class="num">', '').replace('</d>', '').replace('&#x', ' ').replace(';', '').replace('.',' ')
                blist = c.split(' ')
                #print(blist)
                s = ''
                for k in blist:
                    k = k.strip('.')
                    try:
                        if len(k) == 4:
                            tmp = word[k]
                        else:
                            tmp = str(k)
                        s = s + str(tmp)
                    except:
                        pass
                all_list.append(s)
            return all_list
        except:
            return "error"
    #解析地址加密
    def get_address(self,address):
        addstr = ''
        for s in address:
            tmp = s.replace('<e class="address">', ' ').replace('</e>', ' ').replace('<d class="num">', ' ').replace('</d>', ' ').replace(';', '').replace('&#x', '')
            addstr = addstr + str(tmp)
        addlist = addstr.split(' ')
        while '' in addlist:
            addlist.remove('')
        result = ''
        for a in addlist:
            sql = 'select word from woff20190806 where sixteen_key=\'%s\' ;' % (a)
            dbresult = db.select_data(sql)
            if len(dbresult)==0:
                dbresult=a
                result=result+str(a)
            else:
                for a in dbresult:
                    result = result + str(a)
        return result
    def run(self):
            global hreflist
            while len(hreflist)>0:
                print("需要请求的数据还剩："+str(len(hreflist))+'条')
                g_lock.acquire()
                tmp = random.choice(hreflist)
                hreflist.remove(tmp)
                g_lock.release()
                url = "http://" + tmp
                # 根据URL分割得到shopid
                shopid=int(url.split('/')[4])
                # 选取代理IP
                r1 = requests.get('http://47.100.21.174:8899/api/v1/proxies?limit=60').json()
                proxy = random.choice(r1['proxies'])
                try:
                    r = requests.get(url, headers=headers,proxies={'https': 'https://{}:{}'.format(proxy['ip'], proxy['port'])}, timeout=3)
                    r.encoding = 'utf-8'
                    if r.status_code==200:
                        # 店铺名称
                        shopname=re.findall('<title>(.*?)</title>', r.text, re.S)
                        # 均价信息
                        avgPriceTitle = re.findall('<span id="avgPriceTitle" class="item">(.*?)</span>', r.text, re.S)
                        # 点评相关信息
                        comment_score = re.findall('<span class="item">(.*?)</span> ', r.text, re.S)
                        #地址相关信息
                        add=re.findall('<span class="item" itemprop="street-address" id="address">(.*?)</span>', r.text, re.S)

                        #对网页获取内容进行解析
                        sname = g.get_name(shopname)
                        avg=g.get_avg(avgPriceTitle)
                        com=g.get_comment(comment_score)
                        address=g.get_address(add)

                        #根据Xpath方式获取地址 城市 ->行政区->美食分类
                        dom_tree = etree.HTML(r.text)
                        link1 = dom_tree.xpath('//*[@id="body"]/div/div[1]/a[2]/text()')#美食分类
                        link2 = dom_tree.xpath('//*[@id="body"]/div/div[1]/a[3]/text()')#行政区
                        link3 = dom_tree.xpath('//*[@id="body"]/div/div[1]/a[4]/text()')#商圈信息
                        if com!='error':
                            if len(link3)!=0:
                                sql = "insert into shop_tmp(shopid,name,tag,region,area,avg,flavor,envir,service,address) values (%s,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');" % (shopid, sname,
                                       link1[0], link2[0], link3[0],avg.replace('人均', '').replace(':', '').replace('元', ''),com[0].replace('口味', '').replace(':', ''),
                                       com[1].replace('环境', '').replace(':', ''),com[2].replace('服务', '').replace(':', ''),address)
                            else:
                                sql = "insert into shop_tmp(shopid,name,tag,region,avg,flavor,envir,service,address) values (%s,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');" % (
                                    shopid, sname, link1[0], link2[0],
                                    avg.replace('人均', '').replace(':', '').replace('元', ''),
                                    com[0].replace('口味', '').replace(':', ''),
                                    com[1].replace('环境', '').replace(':', ''),
                                    com[2].replace('服务', '').replace(':', ''),
                                    address)
                            print(sql)
                            dbresult=db.inset_data(sql)
                            if dbresult==1:
                                sql="update dzcomment_shop set status=1 where shopid=%s"%(shopid)
                                print(sql)
                                db.inset_data(sql)
                    else:
                        print(r.status_code)
                except Exception as e:
                    print(e)

                time.sleep(random.randint(10,30 ))
class GetURL(threading.Thread):
    def run(self):
        sql = "select DISTINCT (shophref) from dzcomment_shop  where status is NULL;"
        href = db.select_data(sql)
        global hreflist
        hreflist=href
if __name__ == '__main__':
        a=GetURL()
        a.start()
        time.sleep(3)
        g = GetShopInfo()
        g.start()

