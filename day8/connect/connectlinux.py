#!/usr/bin/env python
# coding=utf-8
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('118.24.73.248', 22, username='ubuntu', password='wjq@123456!', timeout=4)
#stdin, stdout, stderr  = client.exec_command('cd /proc;cat meminfo')
stdin, stdout, stderr  = client.exec_command('cd /')
sr = stdout.read()#.decode('utf-8')
print(sr)
print(stderr.read())

