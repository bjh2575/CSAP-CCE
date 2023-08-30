from PyPDF2 import PdfMerger
import win32com.client
import time

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = False


pdf_merger = PdfMerger()

pdf_files = ["C:/Users/user/cloud/mysql_report.pdf",
             "C:/Users/user/cloud/mysql_graph.pdf"]

for pdf_file in pdf_files:
    pdf_merger.append(pdf_file)

output_path = "C:/Users/user/cloud/mysql_result.pdf"
pdf_merger.write(output_path)
pdf_merger.close()
