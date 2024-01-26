import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def envio_mail():
    # Configuración del servidor SMTP
    smtp_host = 'mail.dbjsystem.com'  # Servidor SMTP
    smtp_port = 465  # Puerto para SMTP_SSL
    # Credenciales
    username = 'prueba@dbjsystem.com'  # Nombre de usuario (tu dirección de correo)
    password = '@admin.com'  # Contraseña
    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = 'admin@dbjsystem.com'  # Dirección del destinatario
    msg['Subject'] = 'Entrada al Teletrabajo '
    message = 'Ingreso puntual.'
    msg.attach(MIMEText(message, 'plain'))
    try:
        # Establecer una conexión segura con el servidor SMTP usando SMTP_SSL
        server = smtplib.SMTP_SSL(smtp_host, smtp_port)
        server.login(username, password)  # Iniciar sesión en el servidor SMTP
        text = msg.as_string()
        server.sendmail(msg['From'], msg['To'], text)  # Enviar el correo electrónico
        print("Correo enviado exitosamente!")
    except smtplib.SMTPException as e:
        print(f"Error al enviar correo: {e}")
    finally:
        server.quit()
