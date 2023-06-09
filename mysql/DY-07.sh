#!/bin/bash

# 암호에 SHA-256 이상의 해시 알고리즘이 사용되는지 확인
hash=$(grep '^password.*pam_unix.so' /etc/pam.d/common-password | grep -Po "(?<=sha)[0-9]+")

if test "$hash" = "sha256" && test "$hash" = "sha384" && test "$hash" = "sha512"
then
  # 해시 알고리즘 사용
  result="양호"
else
  # 해시 알고리즘 미사용
  result="취약"
fi

echo "보안 설정,DY-07,안전한 암호화 알고리즘 사용,상,$result" >> my-sql_report.csv