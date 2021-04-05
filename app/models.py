from django.db import models

# Create your models here.
from django.utils.html import format_html


class Jenkins(models.Model):
    name = models.CharField(verbose_name='JOB名称', max_length=128)
    joburl = models.CharField(verbose_name='JOB Url', max_length=250,blank=True, null=True)
    color = models.CharField(verbose_name='图标状态', max_length=25,blank=True, null=True)
    inQueue = models.BooleanField(verbose_name='排队中', default=False, null=True)
    number = models.IntegerField(verbose_name='构建ID',blank=True, null=True)
    result = models.CharField(verbose_name='构建结果', max_length=25,blank=True, null=True)
    buildurl = models.CharField(verbose_name='构建Url', max_length=250,blank=True,null=True)
    building = models.BooleanField(verbose_name='是否构建中', default=False, null=True)
    duration = models.BigIntegerField(verbose_name='耗时(min)',blank=True, null=True)
    estimatedDuration = models.BigIntegerField(verbose_name='预计用时(min)',blank=True , null=True)
    createddate = models.CharField(verbose_name='createddate', max_length=200, blank=True, null=True)
    updateddate = models.CharField(verbose_name='刷新时间', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Jenkins"
        verbose_name_plural = "Jenkins"

    def __str__(self):
        return self.name


    #跳转按钮
    def link_job(self):
        btn_str = '<a  href="{}" target="_blank">link </a> '
        return format_html(btn_str, self.joburl)
    link_job.short_description = 'Job Url'

    #每行增加执行Job按钮
    def exec_job(self):
        btn_str = '<a href="{}" target="_blank" rel="external nofollow" >' \
                  '<input name="执行JOB"' \
                      'type="button" class="el-button el-button--button el-button--small" id="execButton" ' \
                  'title="执行JOB" value="执行JOB">' \
                  '</a>'
        return format_html(btn_str, '{}/build?delay=0sec'.format(self.joburl))
    exec_job.short_description = '执行JOB'

class Money(models.Model):
    name = models.CharField(verbose_name='收支项', max_length=128, help_text='每一笔款项描述')
    dept = models.CharField(verbose_name='dept', max_length=128,default='dept')
    salary = models.BigIntegerField(verbose_name='金额')
    pay = models.BigIntegerField(verbose_name='金额')
    cost = models.BigIntegerField(verbose_name='金额')
    create_date = models.CharField(verbose_name='createddate', max_length=200,blank=True,null=True)

    class Meta:
        verbose_name = "收支"
        verbose_name_plural = "收支记录"

    def __str__(self):
        return self.name


class TestControl(Money): # 父类为要展示的model类
    class Meta:
        proxy = True
        verbose_name = 'TestControl'
        verbose_name_plural = verbose_name

class TestChart1(Money): #
    class Meta:
        proxy = True
        verbose_name = 'TestChart1'
        verbose_name_plural = verbose_name

class TestChart2(Money): #
    class Meta:
        proxy = True
        verbose_name = 'TestChart2'
        verbose_name_plural = verbose_name

class ChartByModel(Money): #
    class Meta:
        proxy = True
        verbose_name = 'ChartByModel'
        verbose_name_plural = verbose_name

class ChartBySql(Money): #
    class Meta:
        proxy = True
        verbose_name = 'ChartBySQL'
        verbose_name_plural = verbose_name
