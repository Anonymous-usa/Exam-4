from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_token(email, token):
    path = f'http://127.0.0.1:8000/auth/confirm-email/{token}'  
    message = f'Click here to confirm your email: {path}'
    try:
        send_mail(
            subject="Welcome to Hamsafar",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )
        return {
            'is_sended': True,
            'message': 'Message sent successfully!'
        }
    except Exception as e:
        return {
            'is_sended': False,
            'message': str(e)
        }