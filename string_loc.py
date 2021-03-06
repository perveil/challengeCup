from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfpage import PDFTextExtractionNotAllowed

def parsePDFtoTXT(pdf_path):
    fp = open(pdf_path,'rb')
    parser = PDFParser(fp)

    # print(parser)

    document= PDFDocument(parser)
    print(document)
    parser.set_document(document)

    # print(parser.set_document(document))
    #
    # document.set_parser(parser)
    # document.initialize()
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr=PDFResourceManager()
        laparams=LAParams()
        device=PDFPageAggregator(rsrcmgr,laparams=laparams)
        interpreter=PDFPageInterpreter(rsrcmgr,device)
        for page in document.get_pages():
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

def get_word_page(word_list):
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
                

parsePDFtoTXT('安图生物-603658_20201030_2的副本.pdf')
get_word_page(['附录','财务报表'])
