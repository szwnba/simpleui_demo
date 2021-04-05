import pymysql
from django.http import HttpResponse
from django.shortcuts import render

from app.models import Money
import sqlite3

from lib.Common import getBitCoin, get_stock_data
from lib.mysql import get_connection


def tesControlview(request):
    return render(request,'admin/tesControl.html')

def testchart1view(request):
    return render(request,'admin/tesChart1.html')

def testchart2view(request):
    df = Money.objects.all()
    month = []
    salary = []
    pay = []
    cost = []
    for info in df:
        month.append(info.name)
        salary.append(info.salary)
        pay.append(info.pay)
        cost.append(info.cost)
    context = {'month': month, 'salary': salary, 'pay': pay, 'cost': cost}
    return render(request,'admin/tesChart2.html', context=context)

def testchartByModelView(request):
    df = Money.objects.all()
    month = []
    salary = []
    pay = []
    cost = []
    for info in df:
        month.append(info.name)
        salary.append(info.salary)
        pay.append(info.pay)
        cost.append(info.cost)

    context = {'month': month, 'salary': salary, 'pay': pay, 'cost': cost}
    return render(request, 'admin/tesChart3.html', context=context)

def testchartBySqlView(request):
    month = []
    dept1 = []
    dept2 = []
    dept3 = []
    # conn = sqlite3.connect('db.sqlite3')
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT name, sum(case when dept='dept1' then 1 else 0 end) as dept1 , sum(case when dept='dept2' then 1 else 0 end) as dept2 , sum(case when dept='dept3' then 1 else 0 end) as dept3 FROM app_money group by name"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        month.append(row[0])
        dept1.append(int(row[1]))
        dept2.append(int(row[2]))
        dept3.append(int(row[3]))
    cursor.close()
    conn.close()
    context = {'month': month, 'dept1': dept1, 'dept2': dept2, 'dept3': dept3}
    return render(request, 'admin/tesChart3.html', context=context)

# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        responseJson =  get_stock_data('sz000829', 30, 30)
        # ctx['rlt'] = "request.POST['q']"
        ctx['rlt'] = responseJson
    return render(request, "admin/tesControl.html", ctx)