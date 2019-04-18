from django.apps import apps
# 表关联不适合
def toUpdate(excludeArray, appName, modelName, obj):
    # 对象形式
    # 过滤显示在页面的字段
    # exclude = ['id', 'type']
    data = []
    modelobj = apps.get_model(appName, modelName)
    if obj == None:
        for i in modelobj._meta.fields:
            if i.name in excludeArray:
                continue
            di = {
                "verbose": i.verbose_name,
                "value": "",
            }
            data.append(di)
        # data数据格式为数组：[{"verbose":"名称","value": ""},  {"verbose":"名称","value": ""}]
        return data
    else:
        # dicc = Student.objects.filter(pk=request.session.get("user_id"))
        dicc = obj.values()[0]

        for (k, v) , i in zip(dicc.items(),modelobj._meta.fields):
            if k in excludeArray:
                continue
            di = {
                "verbose": i.verbose_name,
                "value": v,
            }
            data.append(di)
        # data数据格式为数组：[{"verbose":"名称","value": "属性值"},  {"verbose":"名称","value": "属性值"}]
        return data

# 使用案例 去修改页
# class Detail(View):
#     def get(self, request):
#         # 过滤显示在页面的字段
#         exclude = ['id', 'type', 'isupdate']
#         stuObj = Student.objects.filter(pk=request.session.get("user_id"))
#         data = toUpdate(exclude, "student", "Student", stuObj)
#         return render(request, "user/stuInfo.html",
#                       {"list":data})