from django.shortcuts import render
from django.core.mail import EmailMessage

# Create your views here.
from django.shortcuts import render
from .models import User
from .form import RegistrationForm

def registration(request):
    if request.method != 'POST':
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                exist_user = User.objects.get(email=email)
                if not exist_user.is_active:
                    exist_user.delete()
                else:
                    return render(request, '#', {'error': 'Данный пользователь уже зарегистрирован'})
            except:
                pass

            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # подтверждение через почту
            to_email = email
            mail_subject = 'Ссылка на активацию аккаунта'
            message = 'Проверка отправки сообщений'
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'auth/registrt_email_message.html', {'email': to_email})

    return render(request, 'auth/registration.html', {'form': form})