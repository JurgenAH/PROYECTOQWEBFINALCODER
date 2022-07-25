from django.shortcuts import render


from .models import Producto




# Create your views here.


def tienda(request):    
    
    
    servicios=Producto.objects.all()

    return render(request, "tienda/tienda.html", {"servicios":servicios})