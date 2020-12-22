import pdfplumber
#使用pdfplumber的包将excel的表格导出
import xlwt
import os

def bianli(rootdir):
    for root,dirs,files in os.walk(rootdir):
        #files中以列表的形式存储着当前路径下的文件
        for file in files:
            print(os.path.join(root,file))
            if '.pdf' in os.path.join(root,file):
                excell(os.path.join(root,file))



def excell(path):
# 定义保存Excel的位置
    workbook = xlwt.Workbook()  #定义workbook
    sheet = workbook.add_sheet('Sheet1')  #添加sheet
    i = 0 # Excel起始位置

    print('start')
#pdfPath='688981_20201112_2.pdf'
    #path = '安图生物-603658_20201030_2的副本.pdf'
#path = "aaaaaa.PDF"  # 导入PDF路径
    pdf = pdfplumber.open(path)
    print('\n')
    print('开始读取数据')
    print('\n')
    for page in pdf.pages:
    # 获取当前页面的全部文本信息，包括表格中的文字
    # print(page.extract_text())
        for table in page.extract_tables():
        # print(table)
            for row in table:
                print(row)
                for j in range(len(row)):
                    sheet.write(i, j, row[j])
                i += 1
            print('---------- 分割线 ----------')
    pdf.close()
    # 保存Excel表
    workbook.save(path+'.xls')
    print('\n')
    print('写入excel成功')
    print('保存位置：')
    print('test.xls')
    print('\n')

rootdir='./pdf'
bianli(rootdir)
