import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages

matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # windows
# matplotlib.rcParmas['font.family'] = 'AppleGothic' # mac
matplotlib.rcParams['font.size'] = 15  # 글자크기
# 한글폰트 사용시 마이너스 글자가 깨지는 현상을 해결
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('C:/Users/user/cloud/mysql_report.csv')
graph_path = ('C:/Users/user/cloud/mysql_graph.pdf')

df.fillna('점검 불가', inplace=True)
# 색상 설정
colors = ['#caffbf', '#ffadad', '#ffd6a5']

labels = ['양호', '취약', '점검 불가']

# 계정관리 항목의 점검결과 계산
result1 = df[df['구분'] == '계정관리']['점검결과'].value_counts()
result1 = result1.reindex(['양호', '취약', '점검 불가'], fill_value=0)

# 보안설정의 점검결과 계산
result2 = df[df['구분'] == '보안설정']['점검결과'].value_counts()
result2 = result2.reindex(['양호', '취약', '점검 불가'], fill_value=0)

# 패치 및 로그관리의 점검결과 계산
result3 = df[df['구분'] == '패치 및 로그관리']['점검결과'].value_counts()
result3 = result3.reindex(['양호', '취약', '점검 불가'], fill_value=0)

# 원그래프 데이터 계산
result4 = df['점검결과'].value_counts()
result4 = result4.reindex(['양호', '취약'], fill_value=0)
with PdfPages(graph_path) as pdf:
    # 막대그래프 그리기
    fig, ax = plt.subplots(2, 2, figsize=(8.27, 11.69))

    # Plot for 계정관리
    ax[0, 0].bar(result1.index, result1.values, color=colors, label=labels)
    ax[0, 0].set_title('계정관리')
    ax[0, 0].set_ylim([0, 6])

    # Plot for 보안설정
    ax[0, 1].bar(result2.index, result2.values, color=colors)
    ax[0, 1].set_title('보안설정')
    ax[0, 1].set_ylim([0, 12])

    # Plot for 패치 및 로그관리 관리
    ax[1, 0].bar(result3.index, result3.values, color=colors)
    ax[1, 0].set_title('패치 및 로그관리')
    ax[1, 0].set_ylim([0, 12])
    # 원그래프 그리기
    wedges, _, autotexts = ax[1, 1].pie(
        result4, labels=result4.index, colors=colors, autopct='%1.1f%%', startangle=90)
    ax[1, 1].set_title('My-SQL 진단 결과')
    ax[1, 1].axis('equal')  # 원을 원형으로 보이게 함

    plt.suptitle('My-SQL 취약점 진단 점검 결과', fontsize=25,
                 fontweight='bold', x=0.5, y=0.95)

    fig.subplots_adjust(top=0.8, bottom=0.08, hspace=0.3, wspace=0.3)

    legend_font_size = 12
    fig.legend(labels, loc='center', bbox_to_anchor=(
        0.5, 0.87), ncol=len(labels))

    pdf.savefig()
    plt.close()
