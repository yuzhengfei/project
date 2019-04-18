from datetime import date, datetime
import json

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

# 字符串转成秒数格式："00:00:00"
def timeConvert(str):
    try:
        h, m, s = str.strip().split(":")
    except Exception:
        h, m, s = str.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)