# app/routes.py
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'

mail = Mail(app)

def send_reminder(appointment):
    msg = Message('Appointment Reminder', sender='noreply@example.com', recipients=[appointment.patient.email])
    msg.body = f"Dear {appointment.patient.name},\n\nThis is a reminder for your upcoming appointment on {appointment.date}.\n\nBest regards,\nYour Healthcare Provider"
    mail.send(msg)
