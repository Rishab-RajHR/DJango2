# from django.core.mail import send_mass_mail
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.template.loader import render_to_string

# def send_bulk_email(request):
#     messages1 = ('Welcome User 1', 'Hello User 1', 'Welcome to our platform', 'rr0948555@gmail.com',['krishabraj123@gmail.com'])
#     messages2 = ('Welcome User 1', 'Hello User 1', 'Welcome to our platform', 'rr0948555@gmail.com',['krishabraj43543@gmail.com'])
#     messages3 = ('Welcome User 1', 'Hello User 1', 'Welcome to our platform', 'rr0948555@gmail.com',['krishabraj9876@gmail.com'])
    
#     send_mass_mail((messages1, messages2, messages3), fail_silently=False)
    
#     return HttpResponse("Bulk emails sent successfully!")


def send_bulk_email(request):
    subject = "Welcome to Our Platform"
    from_email = "rr0948555@gmail.com"
    recipient_list = ["krishabraj123@gmail.com","krishabraj543@gmail.com"]
    
    html_content = render_to_string('welcome_email.html',{'username':'Alex'})

    msg = EmailMultiAlternatives(subject, "Welcome to my Platform", from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.attach_file('path/to/your/attachment.pdf')
    msg.send()
    
    return HttpResponse("Bulk email sent successfully!")