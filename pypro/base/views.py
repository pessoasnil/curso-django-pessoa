from django.http import HttpResponse


# from django.shortcuts import render


def home(request):
    # raise ValueError()
    return HttpResponse('<html><body>Olá Django</body></html>', )
