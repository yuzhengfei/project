from datetime import datetime
def get_week_day(date):
  week_day_dict = {
    0: '星期一',
    1: '星期二',
    2: '星期三',
    3: '星期四',
    4: '星期五',
    5: '星期六',
    6: '星期天',
  }
  day = date.weekday()
  return week_day_dict[day]
detester = "2018-05-14"
date = datetime.strptime(detester, "%Y-%m-%d")