import pdfplumber
import xlwt


# 定义保存Excel的位置
workbook = xlwt.Workbook()  #定义workbook
sheet = workbook.add_sheet('Sheet1')  #添加sheet
i = 0 # Excel起始位置

print('start')
#pdfPath='688981_20201112_2.pdf'
path = '安图生物-603658_20201030_2的副本.pdf'
#path = "aaaaaa.PDF"  # 导入PDF路径
pdf = pdfplumber.open(path)
print('\n')
print('开始读取数据')
print('\n')


for page in pdf.pages:

    for table in page.extract_tables():
        print('+++++++++++++++++')
        print(table)
        #table是列表嵌套列表的格式
        print('+++++++++++++++++')
        # for row in table:
        #     print(row)
        #     for j in range(len(row)):
        #         sheet.write(i, j, row[j])
        #     i += 1
        # print('---------- 分割线 ----------')


# pdf.close()


# for page in pdf.pages:
#     # 获取当前页面的全部文本信息，包括表格中的文字
#     # print(page.extract_text())
#     for table in page.extract_tables():
#         print('+++++++++++++++++')
#         print(table)
#         #table是列表嵌套列表的格式
#         print('+++++++++++++++++')
#         for row in table:
#             print(row)
#             for j in range(len(row)):
#                 sheet.write(i, j, row[j])
#             i += 1
#         print('---------- 分割线 ----------')
#
#
# pdf.close()


# 保存Excel表
# workbook.save('tes.xls')
# print('\n')
# print('写入excel成功')
# print('保存位置：')
# print('test.xls')
# print('\n')

