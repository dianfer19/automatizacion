from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
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


def mostrar():
    now = datetime.now()
    fecha_formateada = now.strftime('%d/%m/%Y %H:%M:%S')
    print(f'Hola a las {fecha_formateada}')


scheduler = BlockingScheduler()
scheduler.add_job(envio_mail, 'cron', day_of_week='mon-fri', hour=8, minute=55)

# scheduler.add_job(envio_mail, 'cron', hour=22)
# Ejecuta la funcion todos los días a las 10 am
# scheduler.add_job(mostrar, 'cron', hour=10)

# Ejecuta la funcion especificando un día de la semana y una hora determinada
# scheduler.add_job(mostrar, 'cron', day_of_week='wed', hour=8)
# Ejecuta la funcion especificando varios días de la semana y una hora minuto determinada
# scheduler.add_job(mostrar, 'cron', day_of_week='mon,wed,fri', hour=13, minute=30)
# Ejecuto el primer dia del mes
# scheduler.add_job(mostrar, 'cron', day=1, hour=0)
# trigger por intervalos
# scheduler.add_job(mostrar, 'interval', hours=2)
# scheduler.add_job(mostrar, 'interval', seconds=10)

scheduler.print_jobs()
scheduler.start()
