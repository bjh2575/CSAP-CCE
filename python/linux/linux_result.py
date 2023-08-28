import win32com.client
import time

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = False

from PyPDF2 import PdfMerger

pdf_merger = PdfMerger()

pdf_files = ["C:/Users/Bae/PythonDataWorkspace/project/python/linux_report.pdf", "C:/Users/Bae/PythonDataWorkspace/project/python/linux_graph.pdf"]

for pdf_file in pdf_files:
    pdf_merger.append(pdf_file)

output_path = "C:/Users/Bae/PythonDataWorkspace/project/python/linux_result.pdf"
pdf_merger.write(output_path)
pdf_merger.close()