from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World! Questa è la home page.")

def root(request):
    return HttpResponse("Groot!")

def second_method(request):
    # Questa funzione serve per vedere che le newline non sono considerate :(
    response = 'Benvenuto!\n'
    response += 'Questo è un test.\n'

    return HttpResponse(response)


def get_params(request):
    response = ""
    for k in request.GET:
        response += request.GET[k] + '\n'
    
    return HttpResponse(response)