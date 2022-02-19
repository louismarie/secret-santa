from django.http import HttpResponse

def index():
    return HttpResponse("Alive")
