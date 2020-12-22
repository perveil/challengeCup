
from PyPDF2.pdf import PdfFileReader
import tabula
import pandas as pd

pdfPath='./data/贵州茅台.pdf'
pdf = PdfFileReader(open(pdfPath, "rb"))
page_counts = pdf.getNumPages()
dataframe2 = pd.DataFrame()

pf = tabula.read_pdf(pdfPath, encoding='gbk', multiple_tables=True, pages=52)
print(pf)


