
from django.shortcuts import render
from django.http import HttpResponse
import re


def calculate_bytes(request):
    response = ""
    re_format = r'^R\d{1,3}G\d{1,3}B1d{1,3}$'
    err = ""
    
    try:
        width = int(request.GET.get('w'))
        height = int(request.GET.get('h'))
        format = request.GET.get('format')
    except:
        err = "Errore!"
        return render(request, template_name="img.html", context={"img_size":0, "errstr":err})

    values = re.findall(r'\d{1,3}', format)
    pixel_size = 0
    if(values):
        for v in values:

            # get single pixel size
            pixel_size += int(v)

        
        img_byte_size = (width*height*pixel_size)/8


        ctx = {
            "title": "IMAGE SIZE CALCULATOR",
            "w": width,
            "h": height,
            "f": format,
            "img_size": img_byte_size,
            "errstr": err
        }
        
    
    return render(request, template_name="img.html", context=ctx)


def get_prices(request):
    params = request.GET.get('orders')
    re_prices = r'^[0-9]+\.[0-9]+$'

    prices = re.findall(re_prices, orders)

    ctx = {
        "prices_list": prices
    }

    return render(request, template_name="base.html", context=ctx)

