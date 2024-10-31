import pywhatkit as kit
import schedule
import time

# Lista de contactos (asegúrate de incluir el código de país)
contactos = ["+1234567890", "+0987654321"]  # Reemplaza con los números de tus contactos

# Mensaje a enviar
mensaje = "¡Hola! Este es un recordatorio diario."

# Definir la función de envío
def enviar_mensaje_diario():
    for numero in contactos:
        try:
            # Envía el mensaje inmediatamente (puedes ajustar la hora en el schedule más adelante)
            kit.sendwhatmsg_instantly(numero, mensaje)
            print(f"Mensaje enviado a {numero}")
        except Exception as e:
            print(f"Error al enviar mensaje a {numero}: {e}")

# Programar la tarea diaria a una hora específica
# Cambia "09:00" por la hora deseada en formato de 24 horas, por ejemplo, "15:30" para las 3:30 PM.
schedule.every().day.at("09:00").do(enviar_mensaje_diario)

# Mantener el script en ejecución
print("Automatización de mensajes de WhatsApp iniciada. Presiona Ctrl+C para detener.")
while True:
    schedule.run_pending()  # Ejecuta las tareas programadas
    time.sleep(60)  # Espera 1 minuto antes de verificar de nuevo
