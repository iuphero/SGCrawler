#coding:utf-8
from sgcrawler.crawler import Crawler
from sgcrawler.functions import *
from time import time
import sys, gc
reload(sys)
sys.setdefaultencoding('utf-8')
begin_time = time()


filename = 'sgcrawler/people3.sg'
# filename = 'sgcrawler/people2.sg'
people = parse_file(filename)

config_file = './db.config'
config_group = 'sanguo'
conn = MySQLdb.connect(read_default_file=config_file, read_default_group=config_group)
csr = conn.cursor()

i = 0
for person_list  in people:
    #person_list : name, 统御, 武力, 智力, 政治, 魅力, 出生年 ,死亡年
    #     break
    i +=1
    name = person_list[0]
    crawler = Crawler(name)
    crawler.crawl_all()
    other_list = crawler.get_profile()
    person_list.extend(other_list)
    data = tuple(person_list)
    csr.execute("""
insert into person(name, ts, wl, zl, zz, ml, live_year, die_year, lifetime, sex,
    style_name, native_place, history_dpt, novel_dpt, assessment, office)
     values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """,
    data)
    # if i > 50 and i // 50 == 0:  conn.commit() #每隔50次提交一次
    conn.commit()
    del crawler
    del other_list
    del person_list

# conn.commit()
csr.close()
for miss in Crawler.errorList:
    print miss

total_time = time( ) - begin_time
print '一共用时%s' % total_time
#一共用时908.346048117


