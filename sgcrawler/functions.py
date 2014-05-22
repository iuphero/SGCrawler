#coding:utf-8
import sys, MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')


def parse_file(filename):
    people = []
    conn = open(filename, 'r')
    lines = conn.readlines()
    for line in lines:
        # people[名字] = [名字, 统御, 武力, 智力, 政治, 魅力, 出生年 ,死亡年, sex]
        infos = line.split('#')
        dates = infos[1].split(' ')
        info = infos[0].split(' ')
        lifetime = int(dates[2]) - int(dates[1])
        if(info[2] == '男'):
            sex = '1'
        else:
            sex = '2'
        people.append([info[1], info[4], info[5], info[6], info[7], info[8], dates[1], dates[2], lifetime, sex ])
        # people[info[1]] = [info[1], info[4], info[5], info[6], info[7], info[8], dates[1], dates[2] ]
    conn.close( )
    del lines
    return people






if __name__ == '__main__':
    filename = 'people.sg'
    p = parse_file(filename)
    person = p[0]
    print person
