import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

usuario = 'Python'
senha = 'Senha'
email_base = 'emailbase@gmail.com'
email_destinario = 'emaildestinario@gmail.com'
email_assunto = 'Projeto: Enviar emails com Python'
email_msg = 'O projeto ocorreu corretamente'

mimemsg = MIMEMultipart()

mimemsg['From'] = email_base
mimemsg['To'] = email_destinario
mimemsg['Subject'] = email_assunto
mimemsg.attach(MIMEText(email_msg, 'plain'))

connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
connection.starttls()
connection.login(usuario, senha)
connection.send_message(mimemsg)
connection.quit()
