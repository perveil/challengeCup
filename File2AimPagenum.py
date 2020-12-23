import os
import pdfplumber
import  re
import pandas as pd
def file2pagenum(file_path):
    os.chdir(file_path)
    all_file = os.listdir()
    file2page = {}
    for filename in all_file:
        pdf=pdfplumber.open(filename)
        aim_str_List = str(pdf.pages[1].extract_text()).split("\n")
        aim_str=""
        for sr in aim_str_List:
            if "附录" in sr:
                aim_str=sr
                break
        file2page[filename]=re.findall("\d+", aim_str)[0]
    df = pd.DataFrame(file2page.values(), index=file2page.keys())
    df.to_excel('../index/file2pagenum.xlsx', index=file2page.keys())
    return file2page

file2pagenum("./pdf")
