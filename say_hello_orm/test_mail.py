import smtplib
from email.mime.text import MIMEText
mailto_list=["yunfeix2009@163.com"]
mail_host="smtp.163.com"
mail_user="yunfeix2009@163.com"
mail_pass="VQXNQTMMGOBHCAAO"
mail_postfix="163.com"
mail_ssl_port = 465


def send_mail(to_list, sub, content):
    me="hello"+"<"+mail_user+">"
    msg = MIMEText(content, _subtype='html',_charset='gb2312')
    msg['Subject'] = sub
    msg['Form'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP_SSL(host=mail_host,port=mail_ssl_port)
        s.connect(host=mail_host,port=mail_ssl_port)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False
if __name__ == '__main__':
    if send_mail(mailto_list, "haohaoxuexi", 'tiantianxiangshang'):
        print("successfully sent")
    else:
        print("failed to sent")
