from django.http import HttpResponse
import re

def get_num(request):
    response = 'GET REQUEST: '
    response += request.GET.get('num', 'none')
    return HttpResponse(response)

def get_nome(request):
    response = 'GET REQUEST: '
    response += request.GET.get('nome', 'none')
    return HttpResponse(response)

def greet(request, nome):
    response = f'Welcome back, {nome}!'
    return HttpResponse(response)

def classify_email(request, email):
    prof_email_re = r'^[A-Za-z]+([\.-_]\w)*@unimore\.it$'
    studente_email_re = r'[0-9]{1,6}@studenti\.unimore\.it'
    
    response = ''
    if re.search(prof_email_re, email):
        response = f'L\'email {email} appartiene ad un professore.'
    elif re.search(studente_email_re, email):
        response = f'L\'email {email} appartiene ad uno studente.'
    else:
        response = 'Formato inserito non valido.'

    return HttpResponse(response)