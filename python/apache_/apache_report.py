import textwrap
from matplotlib.table import Table
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages

# 한글 폰트 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15  # 글꼴 크기 조정
matplotlib.rcParams['axes.unicode_minus'] = False

# CSV 파일 경로 설정
report_csv_path = 'C:/Users/user/cloud/apache_report.csv'
solution_csv_path = 'C:/Users/user/cloud/apache_solution.csv'
result_xlsx_path = 'C:/Users/user/cloud/apache_report.xlsx'
result_pdf_path = 'C:/Users/user/cloud/apache_report.pdf'

# 취약점 점검결과 읽어오기
diagnosis_df = pd.read_csv(report_csv_path)
vulnerabilities = diagnosis_df[diagnosis_df['점검결과'] == '취약']['진단코드'].tolist()
diagnosis_df.fillna('N/A', inplace=True)
# 조치사항 읽어오기
actions_df = pd.read_csv(solution_csv_path)

# 조치사항 테이블 생성
table_data = []
for vulnerability in vulnerabilities:
    matching_row = actions_df[actions_df['진단코드'] == vulnerability]
    table_data.append(matching_row.values.flatten().tolist())

col_labels = actions_df.columns.tolist()

# 조치결과 Excel 파일 생성
with pd.ExcelWriter(result_xlsx_path) as writer:
    df = pd.DataFrame(table_data, columns=col_labels)
    diagnosis_df.to_excel(writer, sheet_name='Apache 진단결과')
    df.to_excel(writer, sheet_name='조치사항', index=False)

# 조치결과 PDF 파일 생성
with PdfPages(result_pdf_path) as pdf:
    # Apache 진단결과 시트 (페이지 1)
    fig, ax = plt.subplots(figsize=(8.27, 11.69))  # A4 규격(210mm x 297mm)
    ax.axis('off')
    table = ax.table(
        cellText=diagnosis_df.values[:20], colLabels=diagnosis_df.columns, cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)  # 표 내용 글꼴 크기 조정
    table.scale(1, 4)  # 표 크기 조정

    page_width = 210  # 페이지 너비 (mm)
    page_height = 297  # 페이지 높이 (mm)
    margin = 10  # 여백 크기 (mm)

    column_widths = [0.2, 0.13, 0.41, 0.13, 0.13]

    # 각 행에 열 너비 설정
    for (row, col), cell in table.get_celld().items():
        cell.set_width(column_widths[col])

    ax.set_position([0.1, 0.85, 0.8, 0.8])
    # 표 제목
    title_text = 'Apache 진단결과 (페이지 1)'
    ax.text(0.5, 0.05, title_text, fontsize=18,
            fontweight='bold', ha='center', va='center')
    pdf.savefig()
    plt.close()

    # Apache 진단결과 시트 (페이지 2)
    if len(diagnosis_df) > 20:
        fig, ax = plt.subplots(figsize=(8.27, 11.69))  # A4 규격(210mm x 297mm)
        ax.axis('off')
        ax.set_title('Apache 진단결과 (페이지 2)', fontsize=18)  # 제목 글꼴 크기 조정
        table = ax.table(
            cellText=diagnosis_df.values[20:], colLabels=diagnosis_df.columns, cellLoc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(12)  # 표 내용 글꼴 크기 조정
        table.scale(1, 4)  # 표 크기 조정
        page_width = 210  # 페이지 너비 (mm)
        page_height = 297  # 페이지 높이 (mm)
        margin = 10  # 여백 크기 (mm)

        column_widths = [0.2, 0.13, 0.41, 0.13, 0.13]

        # 각 행에 열 너비 설정
        for (row, col), cell in table.get_celld().items():
            cell.set_width(column_widths[col])

        pdf.savefig()
        plt.close()

    # 조치사항 시트
    fig, ax = plt.subplots(figsize=(8.27, 11.69))  # A4 규격(210mm x 297mm)
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=col_labels,
                     cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(7)  # 표 내용 글꼴 크기 조정
    table.scale(1, 9)  # 표 크기 조정
    ax.set_position([0.1, 0.85, 0.8, 0.8])
    # 표 제목
    title_text = 'Apache 진단결과 (페이지 2)'
    ax.text(0.5, 0.05, title_text, fontsize=18,
            fontweight='bold', ha='center', va='center')

    # 표 내용의 길이를 확인하고 셀에 줄바꿈 추가
    for (row, col), cell in table.get_celld().items():
        if row == 0:  # 헤더 셀은 스킵
            continue
        text = cell.get_text().get_text()
        lines = textwrap.wrap(text, width=55)  # 원하는 너비에 맞춰 텍스트 줄바꿈
        cell.get_text().set_text('\n'.join(lines))

    # 열 별 너비 설정
    column_widths = [0.14, 0.20, 0.66]

    # 각 행에 열 너비 설정
    for (row, col), cell in table.get_celld().items():
        cell.set_width(column_widths[col])

    ax.add_table(table)

    pdf.savefig()
    plt.close()

print("조치결과 PDF 파일이 생성되었습니다.")
