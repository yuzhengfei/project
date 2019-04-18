#图片上传的方法
import random,os
from datetime import datetime

def upload_img(root, request):

    number = random.randint(0, 1000)

    fileName = str(datetime.now())[4:19].replace("-", "").replace(":", "").replace(" ", "") + str(
        number) + request.FILES.get("file", None).name
    destination = open(os.path.join("././media/image/"+root+"/", fileName), 'wb+')
    for chunk in request.FILES.get("file", None).chunks():
        destination.write(chunk)
    destination.close()
    return fileName