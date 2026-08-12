#!/bin/bash
tar -czf etc-backup-$(date +%Y%m%d).tar.gz /etc/
crontab -l
