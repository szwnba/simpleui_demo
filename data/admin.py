from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportActionModelAdmin
from data.models import fuyuzhe, zhihu, guxiaobei, news, tempnews

admin.AdminSite.site_header = '全栈增益系统'
admin.AdminSite.site_title = '全栈增益系统'

@admin.register(news)
class newsAdmin(ImportExportActionModelAdmin):
    list_display = ('id','title','link','type','createddate')
    search_fields = ('title',)
    list_filter = ('type',)
    list_per_page = 20

@admin.register(tempnews)
class tempnewsAdmin(ImportExportActionModelAdmin):
    list_display = ('id','title','link','type','createddate')
    search_fields = ('title',)
    list_filter = ('type',)
    list_per_page = 20

@admin.register(fuyuzhe)
class fuyuzheAdmin(ImportExportActionModelAdmin):
    list_display = ('id','title','link','subtype','checked','createddate')
    search_fields = ('title',)
    list_filter = ('subtype','checked',)
    list_editable = ('checked', )
    # list_display_links = ('title',)
    list_per_page = 50
    # ordering = ('title',)

@admin.register(guxiaobei)
class guxiaobeiAdmin(ImportExportActionModelAdmin):
    list_display = ('id','title','link','subtype','checked','createddate')
    search_fields = ('title',)
    list_filter = ('subtype','checked',)
    list_editable = ('checked', )
    list_per_page = 50
    # ordering = ('title',)

@admin.register(zhihu)
class zhihuAdmin(ImportExportActionModelAdmin):
    list_display = ('itemid','title','link','subtype','star','sent','checked','createddate')
    search_fields = ('title',)
    list_filter = ('subtype',)
    list_display_links = ('itemid',)
    list_editable = ('checked', )
    list_per_page = 20
    ordering = ('-id',)
