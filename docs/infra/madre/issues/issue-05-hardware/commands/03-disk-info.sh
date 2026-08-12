#!/bin/bash
# Info de discos
lsblk -o NAME,MODEL,SERIAL,SIZE,TYPE,MOUNTPOINT
sudo fdisk -l
