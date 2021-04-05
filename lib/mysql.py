import time
import pymysql


def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年", "月", "日")


def get_connection():
    conn = pymysql.connect(host="8.129.115.xx", user="django", passwd="123456", db="django", charset='utf8')
    return conn
