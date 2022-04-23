from multiprocessing import context
from django.shortcuts import render
from APP.models import Diak
from django.contrib.auth.decorators import login_required

# Create your views here.

def VIEW(request):
    
    context = {}

    if request.method == "POST":
        diak_id = request.POST['diakid']
        print(diak_id)
        if diak_id == "0":
            context['vaneinput'] = False
        else:
            context['vaneinput'] = True

            diak = Diak.objects.filter(oktatasi_azonosito = diak_id).first()
            if diak == None:
                context['voltilyen'] = False
            else:
                context['voltilyen'] = True
                
                context['nev'] = diak.nev
                context['pontszam'] = diak.pontszam
                context['A'] = diak.Atagozat
                context['B'] = diak.Btagozat
                context['C'] = diak.Ctagozat
                context['D'] = diak.Dtagozat
                context['E'] = diak.Etagozat
                context['F'] = diak.Ftagozat

                


        

    template="index.html"
    
    
    return render(request, template, context)