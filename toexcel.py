import pdfplumber
import xlwt


# 定义保存Excel的位置
workbook = xlwt.Workbook()  #定义workbook
sheet = workbook.add_sheet('Sheet1')  #添加sheet
i = 0 # Excel起始位置
path = '安图生物-603658_20201030_2的副本.pdf'
pdf = pdfplumber.open(path)

aim_pages=pdf.pages[9:]
for page in pdf.pages[9:]:

    for table in page.extract_tables():
        print('+++++++++++++++++')
        print(table)
        #table是列表嵌套列表的格式
        print('+++++++++++++++++')
        for row in table:
            print(row)
            for j in range(len(row)):
                sheet.write(i, j, row[j])
            i += 1
        print('---------- 分割线 ----------')


pdf.close()

workbook.save('tes.xls')
print('\n')
print('写入excel成功')
print('保存位置：')
print('test.xls')
print('\n')

