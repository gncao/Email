#! /usr/bin/python
# -*- encoding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
username = "security@iflytek.com"
password = "***"
_to = "notify@iflytek.com"

# email
msg = MIMEText("我能吞下玻璃而不伤身体")
msg["Subject"] = "test"
msg["From"] = username
msg["To"] = _to

s = smtplib.SMTP("smtp.iflytek.com", timeout=30)  # 连接smtp邮件服务器,端口默认是25
s.login(username, password)  # 登陆服务器
s.sendmail(username, _to, msg.as_string())  # 发送邮件
s.close()
