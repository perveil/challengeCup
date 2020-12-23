import tabula
import  re
import os


# 获取每一个pdf所对应的附录页码
def file2pagenum(file_path):
    os.chdir(file_path)
    all_file = os.listdir()
    file2page = {}
    for filename in all_file:
        pdfPath = filename
        pf = tabula.read_pdf(pdfPath,multiple_tables=True,encoding='gbk',pages=2)
        file2page[filename]=re.findall("\d+", str(((pf[0].values)[2])[1]))
    return file2page

file2pagenum("./pdf")
