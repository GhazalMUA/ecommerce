import smtplib
from email.message import EmailMessage


EMAIL_HOST = 'smtp.gmail.com'                   #age az gmail estefade mikonin  default hmin  meghdar hastesh. age gheyr az gmail az chizi khastim estefade konim ino bhmoon midan
EMAIL_HOST_PASSWORD ='xnrw lclh zrfy gyos'      #az account gmail khodam yedone gereftam.
EMAIL_HOST_USER = 'hafezibirganighazal@gmail.com'
EMAIL_PORT_SSL = 465


msg=EmailMessage()
msg['Subject']= 'ghazalmua cyberion'
msg['From']= EMAIL_HOST_USER
msg['To']= 'amiroism@gmail.com'
msg.set_content('ghazal')

with smtplib.SMTP_SSL(host=EMAIL_HOST , port=EMAIL_PORT_SSL) as server:
    server.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
    server.send_message(msg)