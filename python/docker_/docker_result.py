from PyPDF2 import PdfMerger
import win32com.client
import time

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = False



pdf_merger = PdfMerger()

pdf_files = ["C:/Users/yoc12/OneDrive/바탕 화면/원본/결과파일/docker_report.pdf", "C:/Users/yoc12/gyuncoding/zzz/docker_graph.pdf"]

for pdf_file in pdf_files:
    pdf_merger.append(pdf_file)

output_path = "C:/Users/yoc12/OneDrive/바탕 화면/원본/결과파일/docker_result.pdf"
pdf_merger.write(output_path)
pdf_merger.close()