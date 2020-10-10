from django.http import HttpResponse


def hello(request, *args, **kwargs):
    return HttpResponse(f"Hello, your user agent is: {request.user_agent}", status=200)


def exception(request, *args, **kwargs):
    raise Exception()
