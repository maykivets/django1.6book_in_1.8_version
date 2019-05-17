# - * - Coding: utf -8 - * -
from django.http import HttpResponse
from django.shortcuts import render


# View for index page.


# def page(request):
#     # return HttpResponse("Hello world!")
#     return render(request, 'en/public/index.html')

def page(request):
    my_variable = "Passed through"
    years_old = 24
    truncate_string = "Welcome in Django "
    array_city = ["Paris", "London", "Washington"]
    return render(request, 'en/public/index.html',
                  {"my_var": my_variable, "years": years_old,
                   "array_city": array_city,
                   "truncate_string": truncate_string})
