#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql


def getCon():
    conn = pymysql.connect(
        host="127.0.0.1",
        user='root',
        password='root',
        database='honor_ini',
        port=3306
    )
    return conn


def selectTest():
    # 连接到mysql数据库
    conn = getCon()

    # 创建游标对象
    cursor = conn.cursor()
    cursor.execute("select * from s_act_7day")
    fields = cursor.description

    # print(fields)
    head = []
    for field in fields:
        head.append(field[0])
    print(head)

    # data = cursor.fetchall()
    # 获取指定条数数据
    rows = cursor.fetchmany(3)
    for row in rows:
        print(row)

    # 关闭游标
    cursor.close()
    conn.close()


if __name__ == '__main__':
    selectTest()
    pass
