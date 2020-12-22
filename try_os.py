import os
def bianli(rootdir):
    for root,dirs,files in os.walk(rootdir):
        #files中以列表的形式存储着当前路径下的文件
        for file in files:
            print(os.path.join(root,file))
            #print(type(os.path.join(root,file)))
        for dir in dirs:
            bianli(dir)
rootdir='./pdf'
bianli(rootdir)

