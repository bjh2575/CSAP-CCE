export LANG=ko_KR.UTF-8
#!/bin/bash

if [ -f /etc/openstack-dashboard/local_settings.py ] ; then
cat /etc/openstack-dashboard/local_settings.py | grep -i "PASSWORD_VALIDATOR" >/dev/null 2>&1
if [ $? -ne 0 ] ; then
echo "보안설정,OT-39,Dashboard의 PASSWORD_VALIDATOR 설정,상,양호">> ./openstack_report.csv
else
echo "보안설정,OT-39,Dashboard의 PASSWORD_VALIDATOR 설정,상,취약">> ./openstack_report.csv
if [ -f etc/openstack-dashboard/local_settings ] ; then
cat /etc/openstack-dashboard/local_settings | grep -i "PASSWORD_VALIDATOR" >/dev/null 2>&1
if [ $? -ne 0 ] ; then
echo "보안설정,OT-39,Dashboard의 PASSWORD_VALIDATOR 설정,상,양호">> ./openstack_report.csv
else
echo "보안설정,OT-39,Dashboard의 PASSWORD_VALIDATOR 설정,상,취약">> ./openstack_report.csv
fi
fi
fi
fi