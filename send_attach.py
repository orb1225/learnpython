#coding=utf-8
from email import encoders
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.mime.base import MIMEBase
import smtplib

msg=MIMEMultipart()
def _format_addr(s):
        name,addr=parseaddr(s)
        return formataddr((Header(name,'utf-8').encode(),addr.encode('utf-8') if isinstance(addr,unicode) else addr))

from_addr="cjy_1225@163.com"
passwd="*******"

to_addr=["121377865@qq.com","1161100759@qq.com"]
smtp_server="smtp.163.com"

msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
with open('Shopee数据需求整理comeon.png', 'rb') as f:
	mime = MIMEBase('image', 'png', filename='test.png')
	mime.add_header('Content-Disposition', 'attachment', filename='test.png')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)


msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
x_1=_format_addr(u'管理员 <%s>' % to_addr[0])
for i in range(1,len(to_addr)):
        x = _format_addr(u'管理员 <%s>' % to_addr[i])
        print x
        x_1=x_1+','+x
        msg['to']=x_1
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, passwd)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()

