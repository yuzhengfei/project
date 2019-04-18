#删除数据库迁移文件
import os
def delete():
    rootArray = os.listdir(os.getcwd().replace("\\utils", "")+"/apps/")
    for root in rootArray:
        file = os.getcwd().replace("\\utils", "")+"/apps/"+root+"/migrations/0001_initial.py"
        if os.path.isfile(file):
            os.remove(file)
    print("删除完毕")

delete()