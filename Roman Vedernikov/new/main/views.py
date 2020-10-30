from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


def index(request):
    data = {
        'title': 'Главная страница',
    }

    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/news/"
    template_name = "main/register.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)
