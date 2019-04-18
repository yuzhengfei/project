# js时间控件
# function checkDate(){
#         var str_date = document.getElementById("str_date").value;
#         var end_date = document.getElementById("end_date").value;
#         if(getDate(str_date)-getDate(end_date)>0){
#             alert("结束时间不能小于开始时间！");
#             return false;
#         }
#     }
#     function getDate(date){
#         var dates = date.split("-");
#         var dateReturn = '';
#         for(var i=0; i<dates.length; i++){
#             dateReturn+=dates[i];
#         }
#         return dateReturn;
#     }
from datetime import datetime
print(type(datetime.now()))