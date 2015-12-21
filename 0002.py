#!/usr/bin/env python3
# coding : utf-8

import string
import pymysql
import random

CodeNum = 200
GroupNum = 4
GroupLen = 4

HOST = "localhost"
USER = "root"
PASSWORDS = "user@password"
PORT = 3306
DB = "test"
Table = "RandomCode"

field = string.ascii_letters + string.digits


def GetOneGroupCode():
    return "".join(random.sample(field, GroupLen))


def GetOneRandomCode():
    return "-".join([GetOneGroupCode() for i in range(GroupNum)])


def Generator(num):
    RandomCode = set()
    for i in range(num):
        RandomCode.add(GetOneRandomCode())
    return RandomCode


def SaveRandomCode(code, TableName):
    con = pymysql.connect(
        host=HOST,
        user=USER,
        passwd=PASSWORDS,
        port=PORT,
        db=DB)
    cur = con.cursor()

    cur.execute("CREATE TABLE "+ str(TableName) +"(id INT, code VARCHAR(255));")
    i = 1
    for c in code:
        SQL = "INSERT INTO " + \
            str(TableName) + " VALUES (%d, '%s');" % (i, str(c))
        cur.execute(SQL)
        i += 1

    cur.close()
    con.commit()
    con.close()


def main():
    SaveRandomCode(Generator(CodeNum), Table)

if __name__ == '__main__':
    main()
