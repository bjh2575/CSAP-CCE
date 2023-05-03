#!/bin/bash

#:진단기준 
#양호 : 로그 기록의 검토, 분석, 리포트 작성 및 보고 등이 정기적으로 이루어지고 있는 경우
#취약 : 로그 기록의 검토, 분석, 리포트 작성 및 보고 등이 정기적으로 이루어지지 않는 경우

#:진단방법
#로그 정책 수립 여부 및 정책에 따른 로그 검토 여부 확인

#:조치방법
#-다음과 같이 로그 파일의 백업에 대한 검토를 해야 함
#1) su 시도에 관한 로그
#2) 반복적인 로그인 실패에 관한 로그
#3) 로그인 거부 메세지에 관한 로그
#4) 기본적 log 파일의 위치는 /var/dam, /var/log


echo "패치 및 로그관리,U-36,로그의 정기적 검토 및 보고,상,$result" >> linux_report.csv