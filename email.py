import smtplib, requests, json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import template_emails

def send_email_verified(email,token,pk,name):
    remitente = 'evansoft.test@gmail.com'
    destinatarios = ["granmaestroismaelsantana@gmail.com",str(email)]
    asunto = 'Validación de cuenta'
    html = 
    html = html.replace("$(token)",str(token))
    html = html.replace("$(pk)",str(pk))
    html = html.replace("$(name)",str(name))
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(html,'html'))
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    usuario = "evansoftservices@gmail.com"
    clave = "xarauthaynkevvpj"
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    sesion_smtp.starttls()
    texto = mensaje.as_string()
    remitente = usuario
    sesion_smtp.login(usuario,clave)
    sesion_smtp.sendmail(remitente, destinatarios, texto)
    sesion_smtp.quit()