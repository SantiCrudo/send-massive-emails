import smtplib
from email.mime.text import MIMEText

# --- 1. CONFIGURACIÓN ---
SMTP_SERVER = 'smtp.gmail.com' # Servidor SMTP de Gmail
SMTP_PORT = 587               # Puerto estándar para TLS
REMITENTE = 'remitente@gmail.com'
DESTINATARIO = 'destinatario@gmail.com'
PASSWORD_APP = '' # ¡Usar clave de aplicación!

ASUNTO = 'Reporte de Automatización Diario'
CUERPO = '¡Hola! Este es un reporte automático generado con Python usando smtplib. La tarea se completó con éxito.'

# --- 2. CREACIÓN DEL MENSAJE ---
# MIMEText ayuda a estructurar el correo con asunto, remitente, etc.
msg = MIMEText(CUERPO)
msg['Subject'] = ASUNTO
msg['From'] = REMITENTE
msg['To'] = DESTINATARIO

# --- 3. CONEXIÓN Y ENVÍO ---
try:
    # 1. Establecer conexión con el servidor
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        
        # 2. Iniciar la encriptación TLS
        server.starttls()
        
        # 3. Iniciar sesión (autenticación)
        server.login(REMITENTE, PASSWORD_APP)
        
        # 4. Enviar el correo
        server.sendmail(REMITENTE, DESTINATARIO, msg.as_string())
        
    print(f"Correo enviado exitosamente a {DESTINATARIO}")

except Exception as e:
    print(f"Ocurrió un error al enviar el correo: {e}")
