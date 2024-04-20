from smtplib import SMTP,SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
import os
from typing import List

host_server='smtp.163.com'
from_email='gxxxxxxxt@163.com'
from_email_pwd='OKWOFSYI98ZWPBN'
utf8_encode='utf-8'
def send_email(to_emails:List, subject:str,body:str,is_html:bool=False,attachment_files:List=[],cc_emails:List=[]):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ','.join(str(email) for email in to_emails)
    msg['CC'] = ','.join(str(email) for email in cc_emails)
    msg['Subject'] = Header(subject,utf8_encode)
    body_type='html' if is_html else 'plain'
    msg_body=MIMEText(body,body_type,utf8_encode)
    msg.attach(msg_body)
    
    for attachment_file in attachment_files:
        file_name=os.path.basename(attachment_file)
        with open(attachment_file,'rb') as f:
            attachment=MIMEText(f.read(),'base64',utf8_encode)
            attachment['Content-Disposition'] = f'attachment; filename="{file_name}"'
            msg.attach(attachment)
    #smtp = SMTP(host_server)
    smtp = SMTP_SSL(host_server)
    smtp.set_debuglevel(1)   # print sending email debug information
    smtp.login(from_email,from_email_pwd)
    smtp.sendmail(from_addr=from_email,to_addrs=to_emails+cc_emails,msg=msg.as_string())
    smtp.quit()
    print('Congratulation! Sending email succeeded')
    

if(__name__=='__main__'):
    send_email(to_emails=['9999@qq.com'],subject='Hello',body='Hi there, see you soon',is_html=False,attachment_files=[r'C:\Users\john_yong\Pictures\tmp\t.jpg'])
    