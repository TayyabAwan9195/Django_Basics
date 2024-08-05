from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client():
    subject="This is Email from django server"
    message="This is a test email From Django Server"
    from_email=settings.EMAIL_HOST_USER
    recipient_list=['plantspointofficial@gmail.com','maliksohailawan113@gmail.com','tayyab.fullstackdev@gmail.com']
    send_mail(subject,message,from_email,recipient_list)