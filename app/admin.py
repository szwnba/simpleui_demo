from datetime import datetime

from django.contrib import admin, messages
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.db import transaction
from django.http import JsonResponse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportActionModelAdmin

from app.GetJenkinsAPI import get_jobs_data
from app.models import TestControl, TestChart1, TestChart2, Money, ChartByModel, ChartBySql, Jenkins
from app.views import tesControlview, testchart1view, testchart2view, testchartByModelView, testchartBySqlView

@admin.register(Jenkins)
class JenkinsAdmin(admin.ModelAdmin):
    list_display = ('name','image_data','inQueue','duration','updateddate','link_job','exec_job')
    list_per_page = 50
    readonly_fields = ('image_data',)

    def image_data(self,obj):
        imageurl="http://192.168.31.85:9001/static/078ab248/images/48x48/red.png"
        if obj.color=="blue_anime":
            imageurl="http://192.168.31.85:9001/static/078ab248/images/48x48/blue_anime.gif"
        elif obj.color=="blue":
            imageurl="http://192.168.31.85:9001/static/078ab248/images/48x48/blue.png"
        else:
            imageurl="http://192.168.31.85:9001/static/078ab248/images/48x48/red.png"
        return mark_safe(u'<img src="%s" style="width: 32px; height: 32px;" />' % imageurl)
    # 页面显示的字段名称
    image_data.short_description = u'执行状态'


    #屏蔽增加按钮
    def has_add_permission(self, request):
        return False

    #屏蔽删除按钮
    def has_delete_permission(self, request, obj=None):
        return False

    # 屏蔽编辑
    def has_change_permission(self, request, obj=None):
        return False

    # 重写changelist_view，不选中选项使用Action
    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and request.POST.get('action') == 'refresh':
            if not request.POST.getlist(ACTION_CHECKBOX_NAME):
                post = request.POST.copy()
                for u in Jenkins.objects.all():
                    post.update({ACTION_CHECKBOX_NAME: str(u.id)})
                request._set_post(post)
        return super(JenkinsAdmin, self).changelist_view(request, extra_context)

    # 增加自定义按钮
    actions = ['refresh']

    def refresh(self, request, queryset):
        # get jenkins data
        job_list = get_jobs_data()
        Jenkins.objects.all().delete()
        for job in job_list:
            Jenkins.objects.create(
                name=job['name'],
                joburl=job['joburl'],
                color=job['color'],
                inQueue=job['inQueue'],
                number=job['number'],
                result=job['result'],
                buildurl=job['buildurl'],
                building=job['building'],
                duration=job['duration'],
                estimatedDuration=job['estimatedDuration'],
                createddate= datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                updateddate= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            )
        # messages.add_message(request, messages.SUCCESS, '更新状态成功')
    refresh.short_description = '刷新Jenkins'
    refresh.icon = 'el-icon-s-promotion'
    # refresh.type ="success"
    refresh.acts_on_all = True

# @admin.register(Money)
class MoneyAdmin(ImportExportActionModelAdmin):
    list_display = ('id','name', 'salary','pay','cost', 'create_date')
    search_fields = ('name',)
    list_filter = ('name',)
    list_display_links = ('name',)
    list_editable = ('salary', 'pay', 'cost')
    # date_hierarchy = 'create_date'
    list_per_page = 20

    @transaction.atomic
    def mybutton(self, request, queryset):
        messages.add_message(request, messages.SUCCESS, '啥也没有~')
        pass
    mybutton.confirm = '您确定要点击测试按钮吗？'

    # 增加自定义按钮
    actions = [mybutton, 'custom_button', 'make_copy','layer_input']

    def custom_button(self, request, queryset):
        pass
    # 显示的文本，与django admin一致
    custom_button.short_description = '测试按钮'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'fas fa-audio-description'
    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'danger'
    # 给按钮追加自定义的颜色
    custom_button.style = 'color:black;'
    # 链接按钮，设置之后直接访问该链接
    # 3中打开方式
    # action_type 0=当前页内打开，1=新tab打开，2=浏览器tab打开
    # 设置了action_type，不设置url，页面内将报错
    custom_button.action_type = 1
    custom_button.action_url = 'https://www.baidu.com'

    def make_copy(self, request, queryset):
        ids = request.POST.getlist('_selected_action')
        for id in ids:
            money = Money.objects.get(id=id)
            Money.objects.create(
                name=money.name,
                salary=money.salary,
                cost=money.cost,
                pay=money.pay
            )
        messages.add_message(request, messages.SUCCESS, '复制成功，复制了{}个员工。'.format(len(ids)))
    make_copy.short_description = '复制员工'

    def layer_input(self, request, queryset):
        # 这里的queryset 会有数据过滤，只包含选中的数据
        post = request.POST
        # 这里获取到数据后，可以做些业务处理
        # post中的_action 是方法名
        # post中 _selected 是选中的数据，逗号分割
        return JsonResponse(data={
            'status': 'success',
            'msg': '处理成功！'
        })

    layer_input.short_description = '弹出对话框输入'
    layer_input.type = 'success'
    layer_input.icon = 'el-icon-s-promotion'

    # 指定为弹出层，这个参数最关键
    layer_input.layer = {
        # 弹出层中的输入框配置
        # 这里指定对话框的标题
        'title': '弹出层输入框',
        # 提示信息
        'tips': '这个弹出对话框是需要在admin中进行定义，数据新增编辑等功能，需要自己来实现。',
        # 确认按钮显示文本
        'confirm_button': '确认提交',
        # 取消按钮显示文本
        'cancel_button': '取消',
        # 弹出层对话框的宽度，默认50%
        'width': '40%',
        # 表单中 label的宽度，对应element-ui的 label-width，默认80px
        'labelWidth': "80px",
        'params': [{
            # 这里的type 对应el-input的原生input属性，默认为input
            'type': 'input',
            # key 对应post参数中的key
            'key': 'name',
            # 显示的文本
            'label': '名称',
            # 为空校验，默认为False
            'require': True
        }]
    }

# @admin.register(TestControl)
class TestControlAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return tesControlview(request)

# @admin.register(TestChart1)
class TestChart1Admin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return testchart1view(request)

# @admin.register(TestChart2)
class TestChart2Admin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return testchart2view(request)

# @admin.register(ChartByModel)
class ChartByModelAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return testchartByModelView(request)

# @admin.register(ChartBySql)
class ChartBySqlAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return testchartBySqlView(request)