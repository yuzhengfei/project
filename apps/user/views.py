# # Create your views here.
# from .models import *
from utils.JsonResponse import response_as_json
from django.views import View
from django.shortcuts import render


# # 去登录页
def toLoginView(request):
    return render(request, "index/index.html")
#
# # 服务器缓存用户身份和用户id
#
# # 创建或修改 session：
# # request.session[key] = value
# # 获取 session：
# # request.session.get(key,default=None)
# # 删除 session
# # del request.session[key]
# # 登录
# class Login(View):
#     def get(self, request):
#         try:
#             username = request.GET.get('username')
#             password = request.GET.get('password')
#             type = request.GET.get('type')
#         except Exception:
#             data = {
#                 'code': 1,
#                 'msg': '参数获取异常！'
#             }
#             return response_as_json(data)
#         try:
#             if int(type) == 1:
#                 stuObj = Student.objects.get(username=username, password=password)
#                 id = stuObj.id
#                 isupdate = stuObj.isupdate
#             elif int(type) == 2:
#                 schoolObj = Teacher.objects.get(username=username, password=password)
#                 id = schoolObj.id
#                 isupdate = schoolObj.isupdate
#             else:
#                 managerObj = Manager.objects.get(username=username, password=password)
#                 id = managerObj.id
#                 isupdate = 1
#             data = {
#                 'code': 0,
#                 'msg': '登录成功！'
#             }
#             request.session['user_id'] = id
#             request.session['type'] = type
#             request.session['isupdate'] = isupdate
#             return response_as_json(data)
#         except Exception:
#             data = {
#                 'code': 1,
#                 'msg': '登录失败！'
#             }
#             return response_as_json(data)
#
# # 去注册页
# class toRegister(View):
#     def get(self, request):
#         return render(request, "index/register.html")
#
# # 注册
# # 1.学生 2.学校 3.企业
# class Register(View):
#     def get(self, request):
#         if int(request.GET.get('type')) == 1:
#             user = {
#                 'username': request.GET.get('username'),
#                 'password': request.GET.get('password'),
#                 'type': request.GET.get('type'),
#             }
#             Student.objects.create(**user)
#         elif int(request.GET.get('type')) == 2:
#             user = {
#                 'username': request.GET.get('username'),
#                 'password': request.GET.get('password'),
#                 'type': request.GET.get('type'),
#             }
#             Teacher.objects.create(**user)
#         else:
#             user = {
#                 'username': request.GET.get('username'),
#                 'password': request.GET.get('password'),
#                 'type': request.GET.get('type'),
#             }
#             Manager.objects.create(**user)
#         data = {
#             'code': 0,
#             'msg': '注册成功！'
#         }
#         return response_as_json(data)
#
# # 去系统页
# class toManager(View):
#     def get(self, request):
#         # request.session['type'] = 2
#         return render(request, "index/manager.html")
