import os
import pdfplumber
import xlwt


def bianli(rootdir):
    for root,dirs,files in os.walk(rootdir):
        workbook = xlwt.Workbook()  #定义workbook
        sheet = workbook.add_sheet('Sheet1')  #添加sheet
        i = 0 # Excel起始位置
        print('start')
        #files中以列表的形式存储着当前路径下的文件
        for file in files:
            path=os.path.join(root,file)
            pdf = pdfplumber.open(path)
            print('\n')
            print('开始读取数据')
            print('\n')
            print(os.path.join(root,file))
            for page in pdf.pages:
            # 获取当前页面的全部文本信息，包括表格中的文字
            # print(page.extract_text())
                for table in page.extract_tables():
                    for row in table:
                        print(row)
                        for j in range(len(row)):
                            sheet.write(i, j, row[j])
                    i += 1
                print('---------- 分割线 ----------')
            pdf.close()

        workbook.save(path+'.xls')
        print('\n')
        print('写入excel成功')
        print('保存位置：')
        print(path+'.xls')
        print('\n')
rootdir='./pdf'
bianli(rootdir)
