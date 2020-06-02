from django.shortcuts import render
from registration.forms import EmployeesForm


def registration(request):
    form = EmployeesForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data

        new_form = form.save()

    return render(request, 'registration/registration.html', locals())
