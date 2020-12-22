from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfpage import PDFPage
#版本问题，其出现了一些变化

pdf_path='安图生物-603658_20201030_2的副本.pdf'

fp = open(pdf_path,'rb')
#创建一个与文档关联的解释器
parser = PDFParser(fp)

print(parser)
#创建一个PDF文档对象
document= PDFDocument(parser)
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
else:
    rsrcmgr=PDFResourceManager()
    laparams=LAParams()
    device=PDFPageAggregator(rsrcmgr,laparams=laparams)
    interpreter=PDFPageInterpreter(rsrcmgr,device)
    print(interpreter)
    for page in PDFPage.get_pages(document):
        print(page)
        interpreter.process_page(page)
        layout=device.get_result()
        print(layout)
        output=str(layout)
        for x in layout:
            if (isinstance(x,LTTextBoxHorizontal)):
                text=x.get_text()
                output+=text
        with open('write.txt','a',encoding='utf-8') as f:
            f.write(output)

word_list=['附录','财务报表']
f=open('write.txt',encoding='utf-8')
text_list=f.read().split('<LTPage')
n=len(text_list)
for w in word_list:
    page_list=[]
    for i in range(1,n):
        if w in text_list[i]:
            page_list.append(i)
    with open('out.txt','a',encoding='utf-8') as f:
            f.write(w+str(page_list)+'\n')


