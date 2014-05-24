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


def get_sgfile_diff(smallfile, bigfile):
    s_conn = open(smallfile,'r')
    b_conn= open(bigfile,'r')
    s_name_set = set()
    b_name_set = set()

    s_lines = s_conn.readlines()
    s_conn.close()
    for line in s_lines:
        snaps = line.split(' ')
        name = snaps[1]
        s_name_set.add(name)
    del s_lines


    b_lines = b_conn.readlines()
    b_conn.close()
    for line in b_lines:
        snaps = line.split(' ')
        name = snaps[1]
        b_name_set.add(name)
    del b_lines

    name_diff_set = b_name_set - s_name_set
    return  name_diff_set

if __name__ == '__main__':
    # filename = 'people.sg'
    # p = parse_file(filename)
    # person = p[0]
    # print person


    diff_set = get_sgfile_diff('people.sg', 'new_people.sg')
    howmany = len(diff_set)
    print 'There is %s diff name:' % howmany
    for name in diff_set:
        print name