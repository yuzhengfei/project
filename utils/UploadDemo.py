# class DeleteNewsViewSet(generics.GenericAPIView):
#     def get(self, request, *args, **kwargs):
#         news_id = int(request.GET.get('id'))
#         newsObj = News.objects.get(id=news_id)
#         news_url = newsObj.news_url
#         os.remove("././media/image/news/" + news_url)
#         newsObj.delete()
#         data = {
#             "code": 0
#         }
#         return response_as_json(data)
#
# class DetailNewsViewSet(generics.GenericAPIView):
#     def get(self, request, *args, **kwargs):
#         PHOTO_URL = server+"/media/image/news/"
#         newsObject = News.objects.get(id=int(request.GET.get('news_id')))
#         urlArray = newsObject.news_url.split(",")
#         urlList = []
#         if urlArray[0] != "":
#             for i in range(len(urlArray)):
#                 PHOTO_URL += urlArray[i]
#                 urlList.append(PHOTO_URL)
#         data = {
#             "code": 0,
#             "publish_name": newsObject.publish_name,
#             "news_title": newsObject.news_title,
#             "news_content": newsObject.news_content,
#             "news_url": urlList,
#             "create_time": newsObject.create_time
#         }
#         return response_as_json(data)
#
#
# from django.utils.encoding import escape_uri_path
# from xlwt import *
# from io import BytesIO
# from datetime import datetime
# from django.http import HttpResponse
#
# #请假条信息导出
# class LeaveExportViewSet(generics.GenericAPIView):
#     def get(self, request, *args, **kwargs):
#         LeaveCourses = LeaveCourse.objects.filter(id__in=request.GET.get('idList').split(','))
#
#         book = Workbook(encoding='utf-8')
#         sheet = book.add_sheet('Sheet')
#         sheet.write(0, 0, label='学生姓名')
#         sheet.write(0, 1, label='课程名')
#         sheet.write(0, 2, label='任课老师')
#         sheet.write(0, 3, label='上课时间')
#         sheet.write(0, 4, label='下课时间')
#         sheet.write(0, 5, label='请假类型')
#         sheet.write(0, 6, label='请假日期')
#         count = 1
#         for leaveCourse in LeaveCourses:
#             sheet.write(count, 0, label=leaveCourse.stu_id.stu_name)
#             sheet.write(count, 1, label=leaveCourse.course_id.course_name)
#             sheet.write(count, 2, label=leaveCourse.course_id.course_teacher)
#             sheet.write(count, 3, label=str(leaveCourse.course_id.course_start_hour)[:19])
#             sheet.write(count, 4, label=str(leaveCourse.course_id.course_end_hour)[:19])
#             sheet.write(count, 5, label=leaveCourse.leave_type)
#             sheet.write(count, 6, label=str(leaveCourse.leave_date)[:19])
#             count+=1
#         sio = BytesIO()
#         book.save(sio)
#         response = HttpResponse()
#         response["Access-Control-Allow-Origin"] = "*"
#         response["Access-Control-Allow-Headers"] = "*"
#         response['Content-Type'] = 'application/vnd.ms-excel'
#         filename = "请假条信息"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+".xls"
#         response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(filename))
#         sio.seek(0)
#         response.write(sio.getvalue())
#         return response