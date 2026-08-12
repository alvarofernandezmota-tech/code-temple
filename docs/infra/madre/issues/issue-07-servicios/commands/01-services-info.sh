#!/bin/bash
systemctl list-units --type=service --state=running
systemctl list-unit-files --type=service --state=enabled
