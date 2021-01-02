# from django.contrib import admin
#
# ################################################
# from spiderApp.models import Proxy
# # class ProxyAdmin(admin.ModelAdmin):
# #     search_fields = ('ip',)  # 指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
# #     list_filter = ('useful',)  # 指定列表过滤器，右边将会出现一个快捷的日期过滤选项，
# admin.site.register(Proxy)#, ProxyAdmin)
# 
# ################################################
# # from spiderApp.models import Brower
# # class BrowerAdmin(admin.ModelAdmin):
# #     search_fields = ('user_agent',"info")  # 指定要搜索的字段，
# #     list_filter = ('useful',)  # 指定列表过滤器，右边将会出现一个快捷的选项
# # admin.site.register(Brower, BrowerAdmin)
# #
# # ################################################
# # from spiderApp.models import Appdata
# # class AppdataAdmin(admin.ModelAdmin):
# #     search_fields = ('app_id','app_store',"app_name","description","category_name")  # 指定要搜索的字段，
# #     list_filter = ("app_store",'category_name',)  # 指定列表过滤器，右边将会出现一个快捷的选项
# # admin.site.register(Appdata, AppdataAdmin)
# #
# # ################################################
# # from spiderApp.models import RequestList
# # class RequestListAdmin(admin.ModelAdmin):
# #     # list_display = ("id","app_store","url","sort","request_type")
# #     search_fields = ('app_store',"url",)  # 指定要搜索的字段，
# #     list_filter = ("app_store",'sort','request_type')  # 指定列表过滤器，右边将会出现一个快捷的选项
# # admin.site.register(RequestList, RequestListAdmin)
# #
# # ################################################
# # from spiderApp.models import Comment
# # class CommentAdmin(admin.ModelAdmin):
# #     # list_display = ("id","app_store","url","sort","request_type")
# #     search_fields = ("comment_id",'app_id',"comment_info",)  # 指定要搜索的字段，
# #     list_filter = ("stars",'app_store')  # 指定列表过滤器，右边将会出现一个快捷的选项
# # admin.site.register(Comment, CommentAdmin)
#
