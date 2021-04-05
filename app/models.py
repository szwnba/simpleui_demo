from django.db import models

# Create your models here.

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
