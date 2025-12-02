# Mail Sender: Automatización de Envío de Correos

## Descripción
Script simple en Python que usa `smtplib` para enviar correos electrónicos de forma automática y segura (vía TLS). Ideal para reportes y notificaciones.

## Requisitos
* **Python 3.x**

## CONFIGURACIÓN DE SEGURIDAD

**NUNCA** uses tu contraseña de correo. Debes generar una **Clave de Aplicación** (App Password) en la configuración de seguridad de tu cuenta de Google.

### Variables a Modificar en el Código:

| Variable | Descripción |
| :--- | :--- |
| `REMITENTE` | Tu email de login. |
| `DESTINATARIO` | Email que recibe el mensaje. |
| `PASSWORD_APP` | **Clave de Aplicación** de 16 caracteres. |
| `ASUNTO`/`CUERPO` | Contenido del mensaje. |

## ▶️ Ejecución
1.  Asegúrate de haber configurado tu `REMITENTE` y `PASSWORD_APP`.
2.  Ejecuta el script:
    ```bash
    python nombre_de_tu_script.py
    ```
