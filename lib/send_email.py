#组装邮件正文
#组装邮件头
#连接smtp服务器并发送

import smtplib #连接smtp服务器并发送邮件
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from conf import config


def send_report():

    #1、组装邮件正文
    msg = MIMEMultipart() #混合合适消息体
    body = MIMEText(config.body,'plain','utf-8')  #plain纯文字html
    msg.attach(body)#将正文添加到msg对象中
    #2、组装邮件头
    msg['From']=config.smtp_server
    msg['To']=config.smtp_user
    msg['Subject']=config.subject
    #4、附件
    with open ("./report/report.html","rb") as f:   #单独执行要用../
        att_file = f.read()
    att = MIMEText(att_file, 'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream' # 声明附件的内容格式 MIME数据流格式
    att["Content-Disposition"] = "attachment;filename='report.html'" # 附件描述信息 filename是附件显示的文件名
    msg.attach(att) #将附件添加到消息对象中
    #3、连接smtp服务器并发送
    smtp = smtplib.SMTP(config.smtp_server) # 建立连接
    smtp.login(config.smtp_user, config.smtp_password) # 登录邮箱
    # smtp.sendmail("ivan-me@163.com",
    #               'superhin@126.com',
    #               msg.as_string())  # 讲MIME格式邮件转成字符串发送
    smtp.sendmail(config.smtp_user,
                  config.smtp_user,
                  msg.as_string())  # 讲MIME格式邮件转成字符串发送