import logging
import os

import PyPDF2


# 寻找目录下所有的pdf文档
def find_pdf_files(directory):
    directory = os.path.abspath(directory)
    logging.info("工作路径是:" + directory)
    fileList = []
    lists = os.listdir(directory)
    for i in lists:
        if i.endswith(".pdf"):
            filePath = os.path.join(directory, i)
            fileList.append(filePath)
    return fileList


# 将所有文件下的pdf从第二页开始添加到列表中
def add_pages_to_pdf_list(fileList):
    pdfPage_list = []
    for pdfFile in fileList:
        pp = PyPDF2.PdfFileReader(open(pdfFile, 'rb'))
        logging.info("现在在处理:" +pdfFile)
        for page in range(1, pp.getNumPages()):
            pdfPage_list.append(pp.getPage(page))
    return pdfPage_list

# 创建一个新的pdf文件
def create_new_pdf(pdfpage_list,filepath):

    with open(filepath,'wb') as outfile:
        ppp = PyPDF2.PdfFileWriter()
        for i in range(len(pdfpage_list)):
            ppp.addPage(pdfpage_list[i])
        ppp.write(outfile)

# 获取页面内容
def get_page_content(num,pdfpage_list):

    print(pdfpage_list[num].extractText())


# p1 = PyPDF2.PdfFileReader(open("./meetingminutes.pdf", "rb"))
# p2 = PyPDF2.PdfFileWriter(open("./meetingminutes2.pdf", "wb"))
# r2 = PyPDF2.PdfFileWriter(open("./meetingminutes2.pdf", "rb"))
#
# for page in range(1, p1.getNumPages()):
#     p2.addPage(p1.getPage(page))
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
print("haha")
pdf_list = find_pdf_files("./")
pdfpage_list = add_pages_to_pdf_list(pdf_list)
get_page_content(2,pdfpage_list)