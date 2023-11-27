from django.shortcuts import render, redirect
from django.core.mail import send_mail


def example(request):
    return render(request, 'index.html')


def send_massage(request):
    if request.method == 'POST':
        email = request.POST['email']
        massage = request.POST['massage']
        send_mail(
            'Jvokh1r Company',
            massage,
            'setting.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )
        return redirect('example')
