from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.user.is_authenticated:
        return HttpResponse("hello, worl. you're at the authzapp index")
    else:
        if request.user is None:
            return HttpResponse("hello, user is None")
        else:
            headers = ','.join(request.META)
            if 'HTTP_AUTHORIZATION' in request.META:
                msg = "header auth is {} - headers({})".format(
                        request.META['HTTP_AUTHORIZATION'], headers)
            else:
                msg = "hello, user is {} - headers({})".format(
                        request.user, headers)

            return HttpResponse(msg)

