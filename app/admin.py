from django.contrib import admin, messages
from django.db import transaction
from django.http import JsonResponse
from import_export.admin import ImportExportActionModelAdmin

from app.models import TestControl, TestChart1, TestChart2, Money, ChartByModel, ChartBySql
from app.views import tesControlview, testchart1view, testchart2view, testchartByModelView, testchartBySqlView



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