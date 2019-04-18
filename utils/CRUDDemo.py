# 学生列表
class StuList(View):
    def get(self, request):
        return render(request, "manager/ManagerStuList.html",
                      {"list":Student.objects.all()})

# 删除老师
class DelTea(View):
    def get(self, request):
        Teacher.objects.get(pk=request.GET.get("teaId")).delete()
        return response_as_json(data={"code":0})

# 添加公告
class AddNotice(View):
    def get(self, request):
        dic = {
            "publisher": Manager.objects.get(pk=request.session.get("user_id")),
            "title": request.GET.get("str1"),
            "content": request.GET.get("str2"),
            "start_time": request.GET.get("str3"),
            "end_time": request.GET.get("str4"),
        }
        Notice.objects.create(**dic)
        return response_as_json({"code": 0})

# 我的课题
class MyTopic(View):
    def get(self, request):
        # 显示老师审核通过后的课题
        sql = "SELECT * FROM t_result WHERE status='通过' AND " \
              "stuById_id=" + str(request.session.get("user_id"))
        results = Result.objects.raw(sql)
        return render(request, "topic/stuMyTopic.html",
                      {"list": results})

# 审核状态 数据取未通过或者待审核
class Status(View):
    def get(self, request):
        stuObj = Student.objects.filter(pk=request.session.get("user_id"))
        # try:
        sql = "SELECT * FROM t_result WHERE (status='待审核' OR status='未通过') AND " \
              "stuById_id=" + str(request.session.get("user_id"))
        results = Result.objects.raw(sql)
        return render(request, "topic/stuStatusTopic.html",
                      {"list": results})