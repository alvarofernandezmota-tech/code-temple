#!/bin/bash
systemctl list-units | grep -iE "(prometheus|grafana|node|zabbix|nagios)"
ps aux | grep -iE "(prometheus|grafana|node|zabbix|nagios)"
