from django.db import models

class news(models.Model):
    itemid = models.BigIntegerField(verbose_name='itemid',blank=True,null=True)
    title = models.CharField(verbose_name='title', max_length=500,null=True)
    link = models.CharField(verbose_name='link', max_length=500,null=True)
    type = models.CharField(verbose_name='type', max_length=50,blank=True,null=True)
    subtype = models.CharField(verbose_name='subtype', max_length=50,blank=True,null=True)
    star = models.IntegerField(default=0)
    sent = models.IntegerField(default=0)
    checked = models.BooleanField(verbose_name='checked', default=False)
    keywords = models.CharField(verbose_name='keywords', max_length=50,blank=True,null=True)
    comment = models.CharField(verbose_name='comment', max_length=2000,blank=True,null=True)
    createddate = models.CharField(verbose_name='createddate', max_length=200,blank=True,null=True)
    updateddate = models.CharField(verbose_name='updateddate', max_length=200,blank=True,null=True)

    class Meta:
        verbose_name = "news"
        verbose_name_plural = "独立站信息"
    def __str__(self):
        return self.title

class tempnews(models.Model):
    itemid = models.BigIntegerField(verbose_name='itemid',blank=True,null=True)
    title = models.CharField(verbose_name='title', max_length=500,null=True)
    link = models.CharField(verbose_name='link', max_length=500,null=True)
    type = models.CharField(verbose_name='type', max_length=50,blank=True,null=True)
    subtype = models.CharField(verbose_name='subtype', max_length=50,blank=True,null=True)
    star = models.IntegerField(default=0)
    sent = models.IntegerField(default=0)
    checked = models.BooleanField(verbose_name='checked', default=False)
    keywords = models.CharField(verbose_name='keywords', max_length=50,blank=True,null=True)
    comment = models.CharField(verbose_name='comment', max_length=2000,blank=True,null=True)
    createddate = models.CharField(verbose_name='createddate', max_length=200,blank=True,null=True)
    updateddate = models.CharField(verbose_name='updateddate', max_length=200,blank=True,null=True)

    class Meta:
        verbose_name = "tempnews"
        verbose_name_plural = "临时信息"
    def __str__(self):
        return self.title

class fuyuzhe(models.Model):
    itemid = models.BigIntegerField(verbose_name='itemid',blank=True,null=True)
    title = models.CharField(verbose_name='title', max_length=500,null=True)
    link = models.CharField(verbose_name='link', max_length=500,null=True)
    type = models.CharField(verbose_name='type', max_length=50,blank=True,null=True)
    subtype = models.CharField(verbose_name='subtype', max_length=50,blank=True,null=True)
    star = models.IntegerField(default=0)
    sent = models.IntegerField(default=0)
    checked = models.BooleanField(verbose_name='checked', default=False)
    keywords = models.CharField(verbose_name='type', max_length=50,blank=True,null=True)
    comment = models.CharField(verbose_name='comment', max_length=2000,blank=True,null=True)
    createddate = models.CharField(verbose_name='createddate', max_length=200,blank=True,null=True)
    updateddate = models.CharField(verbose_name='updateddate', max_length=200,blank=True,null=True)

    class Meta:
        verbose_name = "fuyuzhe"
        verbose_name_plural = "富裕者联盟"

    def __str__(self):
        return self.title


class guxiaobei(models.Model):
    itemid = models.BigIntegerField(verbose_name='itemid',blank=True,null=True)
    title = models.CharField(verbose_name='title', max_length=500,null=True)
    link = models.CharField(verbose_name='link', max_length=500,null=True)
    type = models.CharField(verbose_name='type', max_length=50,blank=True,null=True)
    subtype = models.CharField(verbose_name='subtype', max_length=50,blank=True,null=True)
    star = models.IntegerField(default=0)
    sent = models.IntegerField(default=0)
    checked = models.BooleanField(verbose_name='checked', default=False)
    keywords = models.CharField(verbose_name='keywords', max_length=50,blank=True,null=True)
    comment = models.CharField(verbose_name='comment', max_length=2000,blank=True,null=True)
    createddate = models.CharField(verbose_name='createddate', max_length=200,blank=True,null=True)
    updateddate = models.CharField(verbose_name='updateddate', max_length=200,blank=True,null=True)

    class Meta:
        verbose_name = "guxiaobei"
        verbose_name_plural = "顾小北博客"

    def __str__(self):
        return self.title


class zhihu(models.Model):
    itemid = models.BigIntegerField(verbose_name='itemid',blank=True,null=True)
    title = models.CharField(verbose_name='title', max_length=500,null=True)
    link = models.CharField(verbose_name='link', max_length=500,null=True)
    type = models.CharField(verbose_name='type', max_length=50,blank=True,null=True)
    subtype = models.CharField(verbose_name='subtype', max_length=50,blank=True,null=True)
    star = models.IntegerField(default=0)
    sent = models.IntegerField(default=0)
    checked = models.BooleanField(verbose_name='checked', default=False)
    keywords = models.CharField(verbose_name='keywords', max_length=50,blank=True,null=True)
    comment = models.CharField(verbose_name='comment', max_length=2000,blank=True,null=True)
    createddate = models.CharField(verbose_name='createddate', max_length=200,blank=True,null=True)
    updateddate = models.CharField(verbose_name='updateddate', max_length=200,blank=True,null=True)

    class Meta:
        verbose_name = "zhihu"
        verbose_name_plural = "知乎"
    def __str__(self):
        return self.title
